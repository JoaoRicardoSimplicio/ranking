from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
from tqdm import tqdm
import requests

from overall.instagram import get_url_instagram
from overall.teams import save_teams
from overall.models import Team


class Command(BaseCommand):
	help = """
	 	You can use this command to extract information about nfl teams. 
	 	Such as name, nfl profile page and instagram profile link.
	"""


	def add_arguments(self, parser):
		parser.add_argument(
				'--refresh',
		    	default=False,
		    	help='refresh all teams from nfl in database'
		)


	def handle(self, *args, **kwargs):
		try:
			self.teamsList = self.extract_teams()
			if kwargs.get('refresh') == 'True' or kwargs.get('refresh') == 'true':
				save_teams(self.teamsList, refresh=True)
			else:
				save_teams(self.teamsList, refresh=False)
		except Exception:
			CommandError("Error with command")
		

	def extract_teams(self):
		print("step 1: Get all teams in nfl site...")
		urlNflSite = 'https://www.nfl.com'
		urlNflTeams = 'https://www.nfl.com/teams/'
		teamsList = []
		response = requests.get(urlNflTeams)
		result = BeautifulSoup(response.content, 'html.parser').find_all("div", class_ ="d3-o-media-object__body nfl-c-custom-promo__body")
		for dataTeams in tqdm(result):
			team = {
				'name': dataTeams.p.text,
				'site_profile_link': urlNflSite + dataTeams.find("a", class_ ="d3-o-media-object__link d3-o-button nfl-o-cta nfl-o-cta--primary").get('href'),
				'instagram_link': get_url_instagram(dataTeams.p.text),
				'sport' : 'american football',
				'country': 'united states'
			}
			if team['instagram_link'] is not None:
				teamsList.append(team)
		return teamsList




