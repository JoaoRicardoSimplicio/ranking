from django.core.management.base import BaseCommand, CommandError
import requests
import json
from bs4 import BeautifulSoup
from tqdm import tqdm

from overall.instagram import get_url_instagram
from overall.teams import save_teams
from overall.models import Team

class Command(BaseCommand):
    help = """
        You can use this command to extract information about premier league teams.
        Such as name, premier league profile page and instagram profile link.
    """

    def add_arguments(self, parser):
        parser.add_argument(
            '--refresh',
            default=False,
            help='refresh all teams from premier league in database'
        )

    def handle(self, *args, **kwargs):
        try:
            self.teamsList = self.extract_teams()
            if kwargs['refresh'] == 'True' or kwargs['refresh'] == 'true':
                save_teams(self.teamsList, refresh=True)
            else:
                save_teams(self.teamsList, refresh=False)
        except Exception:
            pass


    def get_list_wrong_instagrams(self):
        try:
            with open('list_instagram_wrong.json') as f:
                print(f)
                result = json.load(f)
            return result
        except Exception as Error:
            print(Error)


    def extract_teams(self):
        print("step 1: Get all teams in premier league site...")
        urlPremierLeagueSite = 'https://www.premierleague.com/'
        urlPremierLeagueTeams = 'https://www.premierleague.com/clubs/'
        listWrongInstagrams = self.get_list_wrong_instagrams()
        teamsList = []
        response = requests.get(urlPremierLeagueTeams)
        result = BeautifulSoup(response.content, 'html.parser').find('ul', class_ ='clubList').find_all('li')
        for dataTeams in tqdm(result):
            team = {
                'name': dataTeams.span.text,
                'site_profile_link': (dataTeams.a.get('href')).replace(" ", ''),
                'instagram_link': get_url_instagram(dataTeams.span.text),
                'sport': 'football',
                'country': 'england'
            }
            if team['name'] in listWrongInstagrams['teamsList']:
                team['instagram_link'] = listWrongInstagrams['teamsList'][team['name']]['instagram_link']
            teamsList.append(team)
        return teamsList
