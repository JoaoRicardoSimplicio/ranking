from django.core.management.base import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup
import json
from tqdm import tqdm

from nfl.models import nflTeams

class Command(BaseCommand):
	help = "You can use this command to extract information about nfl teams. Such as name, nfl profile page and instagram profile link"

	def add_arguments(self, parser):
		parser.add_argument(
			'--refresh',
			default=False,
			help='refresh all teams in database'
		)


	def handle(self, *args, **kwargs):
		self.teamsList = self.extract_teams()
		if kwargs.get('refresh') == 'True' or kwargs.get('refresh') == 'true':
			self.save_teams(self.teamsList, refresh=True)
		else:
			self.save_teams(self.teamsList, refresh=False)
	

	def get_url_instagram(self, name):
		response = requests.get('https://www.instagram.com/web/search/topsearch/?context=blended&query={}' .format(name))
		result = json.loads(response.content)
		for account in result['users']:
			if account['user']['is_verified'] == True and account['user']['is_private'] == False:
				username = account['user']['username']
				break
		instagramUrlTeam = 'https://www.instagram.com/{}/'.format(username)
		return instagramUrlTeam


	def extract_teams(self):
		print("step 1: Get all teams in nfl site...")
		urlBase = 'https://www.nfl.com'
		urlNflTeams = 'https://www.nfl.com/teams/'
		teams = []
		response = requests.get(urlNflTeams)
		result = BeautifulSoup(response.content, 'html.parser').find_all("div", class_ ="d3-o-media-object__body nfl-c-custom-promo__body")
		for dataTeams in tqdm(result):
			team = {
				'name': dataTeams.p.text,
				'nfl_profile_link': urlBase + dataTeams.find("a", class_ ="d3-o-media-object__link d3-o-button nfl-o-cta nfl-o-cta--primary").get('href')
			}
			instagramProfileLink = self.get_url_instagram(team.get('name'))
			team['instagram_link'] = instagramProfileLink
			teams.append(team)
		return teams


	def save_teams(self, teamsList, **kwargs):
		print("step 2: Save all teams...")
		for team in tqdm(teamsList):
			newTeam = nflTeams(name=team.get('name'), nfl_profile_link=team.get('nfl_profile_link'), instagram_link=team.get('instagram_link'))
			if not nflTeams.objects.filter(name=newTeam.name).exists() and kwargs.get('refresh') != True:
				newTeam.save()
			elif nflTeams.objects.filter(name=newTeam.name).exists() and kwargs.get('refresh') == True:
				previousInstanceTeam = nflTeams.objects.get(name=newTeam.name)
				previousInstanceTeam.name = newTeam.name
				previousInstanceTeam.nfl_profile_link = newTeam.nfl_profile_link
				previousInstanceTeam.instagram_profile_link = newTeam.instagram_link
				previousInstanceTeam.save()
			elif not nflTeams.objects.filter(name=newTeam.name).exists() and kwargs.get('refresh') == True:
				newTeam.save()
			else:
				pass



