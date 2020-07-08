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
        urlLaLigaSite = 'https://www.laliga.com/'
        urlLaLigaTeams = 'https://www.laliga.com/laliga-santander/clubes/'
        listWrongInstagrams = self.get_list_wrong_instagrams()
        teamsList = []
        response = requests.get(urlLaLigaTeams)
        result = BeautifulSoup(response.content, 'html.parser').select('.styled__ItemContainer-sc-1el5vkx-2')
        for dataTeams in tqdm(result):
            if dataTeams.h2.text not in listWrongInstagrams['teamsList']:
                instagramLink = get_url_instagram(dataTeams.h2.text.lower())
            elif dataTeams.h2.text in listWrongInstagrams['teamsList']:
                instagramLink = listWrongInstagrams['teamsList'][dataTeams.h2.text]['instagram_link']
            team = {
                'name': dataTeams.h2.text,
                'site_profile_link': f'{urlLaLigaSite}{dataTeams.get("href")}',
                'instagram_link': instagramLink,
                'sport': 'football',
                'country': 'spain'
            }
            if team['instagram_link'] is not None:
                teamsList.append(team)
        return teamsList
