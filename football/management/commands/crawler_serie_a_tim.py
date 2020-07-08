from django.core.management.base import BaseCommand, CommandError
import requests
import json
from bs4 import BeautifulSoup
from tqdm import tqdm

from overall.instagram import get_url_instagram
from overall.teams import save_teams

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        try:
            self.teams = self.get_all_team_data()
            save_teams(self.teams)
        except:
            return None


    def get_list_wrong_instagrams(self):
        try:
            with open('list_instagram_wrong.json') as f:
                result = json.load(f)
            return result
        except Exception as Error:
            print(Error)


    def get_page_seriea_tim(self):
        response = requests.get('http://www.legaseriea.it/en/serie-a/league-table')
        return response


    def get_teams_in_page(self):
        teamsList = []
        response = self.get_page_seriea_tim()
        results = [element.find_all('img') for element in BeautifulSoup(response.content, 'html.parser').find_all("table", class_="classifica")][0]
        for result in results:
            teamsList.append(result.get('title').lower())
        return teamsList


    def get_all_team_data(self):
        listWrongInstagrams = self.get_list_wrong_instagrams()
        nameTeamList = self.get_teams_in_page()
        teamsList = []
        for nameTeam in nameTeamList:
            if nameTeam not in listWrongInstagrams['teamsList']:
                instagramLink = get_url_instagram(nameTeam)
            elif nameTeam in listWrongInstagrams['teamsList']:
                instagramLink = listWrongInstagrams['teamsList'][nameTeam]['instagram_link']
            team = {
                'name': nameTeam,
                'site_profile_link': f'http://www.legaseriea.it/en/serie-a/teams/{nameTeam}',
                'sport': 'football',
                'country': 'italy',
                'instagram_link': instagramLink
            }
            if team['instagram_link'] is not None:
                teamsList.append(team)
        return teamsList


        


    