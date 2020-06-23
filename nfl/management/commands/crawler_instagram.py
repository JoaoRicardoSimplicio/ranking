import requests
import json
from django.core.management.base import BaseCommand, CommandError
from nfl.models import nflTeams, nflInstagrams
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.teamsList = nflTeams.objects.all()
        self.teamsInstagramList = self.get_instagram_information(self.teamsList)
        self.save_instagram_information(self.teamsInstagramList)


    def save_instagram_information(self, teamsInstagramList):
        print("step 2: Save all instagram accounts...")
        for team in tqdm(teamsInstagramList):
            if team.get('profile_private') == False and team.get('profile_verifyed') == True:
                if not nflInstagrams.objects.filter(team=team.get('team')).exists():
                    newTeam = nflInstagrams(
                        team = team.get('team'),
                        followers = team.get('followers'),
                        followings = team.get('followings'),
                        username = team.get('username'),
                        profile_picture = team.get('profile_picture'),
                        profile_verifyed = team.get('profile_verifyed')
                    )
                    newTeam.save()
                else:
                    previousTeamInstance = nflInstagrams.objects.get(team=team.get('name'))
                    previousTeamInstance.followers = team.get('followers')
                    previousTeamInstance.followings = team.get('followings')
                    previousTeamInstance.profile_picture = team.get('profile_picture')
                    previousTeamInstance.save()


    def transform_instagram_information(self, team, profileInformation):
        instagramTeamInformation = {
            'team': team,
            'followers': profileInformation['edge_followed_by']['count'],
            'followings': profileInformation['edge_follow']['count'],
            'username': profileInformation['username'],
            'profile_picture': profileInformation['profile_pic_url_hd'],
            'profile_verifyed': profileInformation['is_verified'],
            'profile_private': profileInformation['is_private'],
            'overall_category_name': profileInformation['overall_category_name']
        }
        return instagramTeamInformation


    def get_instagram_information(self, teamsList):
        teamsInstagramList = []
        print("Step 1: Get all instagram accounts...")
        for team in tqdm(teamsList):
            response = requests.get(team.instagram_link)
            result = str(BeautifulSoup(response.content, 'html.parser').select('script'))
            dataInstagram = json.loads(result.split('window._sharedData = ')[1].split(';</script>, <script')[0])
            profileInformation = dataInstagram['entry_data']['ProfilePage'][0]['graphql']['user']
            instagramTeamInformation = self.transform_instagram_information(team, profileInformation)
            teamsInstagramList.append(instagramTeamInformation)
            time.sleep(10)
        return teamsInstagramList