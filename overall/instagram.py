import requests
import json
from bs4 import BeautifulSoup
from tqdm import tqdm
import time

from .models import Instagram


def get_url_instagram(teamName):
    response = requests.get(
	    'https://www.instagram.com/web/search/topsearch/?context=blended&query={}' .format(teamName))
    result = json.loads(response.content)
    try:
        for account in result['users']:
            if account['user']['is_verified'] is True and account['user']['is_private'] is False:
                username = account['user']['username']
                break
        instagramUrlTeam = 'https://www.instagram.com/{}/'.format(username)
        return instagramUrlTeam
    except Exception:
        return None


def transform_information_from_instagram(team, profileInformation):
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


def get_instagram_information(teamsList):
    teamsInstagramList = []
    print("Step 1: Get all instagram accounts...")
    for team in tqdm(teamsList):
        response = requests.get(team.instagram_link)
        result = str(BeautifulSoup(response.content, 'html.parser').select('script'))
        dataInstagram = json.loads(result.split('window._sharedData = ')[1].split(';</script>, <script')[0])
        profileInformation = dataInstagram['entry_data']['ProfilePage'][0]['graphql']['user']
        instagramTeamInformation = transform_information_from_instagram(team, profileInformation)
        teamsInstagramList.append(instagramTeamInformation)
        time.sleep(10)
    return teamsInstagramList


def save_instagram_information(teamsInstagramList):
    print("step 2: Save all instagram accounts...")
    for team in tqdm(teamsInstagramList):
        if team.get('profile_private') == False and team.get('profile_verifyed') == True:
            if not Instagram.objects.filter(team=team.get('team')).exists():
                newTeam = Instagram(
                    team = team.get('team'),
                    followers = team.get('followers'),
                    followings = team.get('followings'),
                    username = team.get('username'),
                    profile_picture = team.get('profile_picture'),
                    profile_verifyed = team.get('profile_verifyed')
                )
                newTeam.save()
            else:
                previousTeamInstance = Instagram.objects.get(team=team.get('team'))
                previousTeamInstance.followers = team.get('followers')
                previousTeamInstance.followings = team.get('followings')
                previousTeamInstance.username = team.get('username')
                previousTeamInstance.profile_picture = team.get('profile_picture')
                previousTeamInstance.save()


