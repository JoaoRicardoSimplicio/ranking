from django.core.management.base import BaseCommand, CommandError
import requests
from bs4 import BeautifulSoup
import json

from nfl.models import nflTeams

class Command(BaseCommand):
	help = "You can use this command to extract information about nfl teams. Such as name, nfl profile page and instagram profile link"
	def handle(self, *args, **kwargs):
		self.teams = self.extract_teams()
		self.save_teams(self.teams)
	

	def get_url_instagram(self, name):
		response = requests.get('https://www.instagram.com/web/search/topsearch/?context=blended&query={}' .format(name))
		result = json.loads(response.content)
		for account in result['users']:
			if account['user']['is_verified'] == True and account['user']['is_private'] == False:
				username = account['user']['username']
				break
		instagram_url = 'https://www.instagram.com/{}/'.format(username)
		return instagram_url



	def extract_teams(self):
		url = 'https://www.nfl.com/teams/'
		teams = []
		response = requests.get(url)
		result = BeautifulSoup(response.content, 'html.parser').find_all("div", class_ ="d3-o-media-object__body nfl-c-custom-promo__body")
		for data_teams in result:
			team = {
				'name': data_teams.p.text,
				'nfl_profile_link': url + data_teams.find("a", class_ ="d3-o-media-object__link d3-o-button nfl-o-cta nfl-o-cta--primary").get('href')
			}
			instagram_profile_link = self.get_url_instagram(team.get('name'))
			team['instagram_link'] = instagram_profile_link
			teams.append(team)
		return teams


	def save_teams(self, teams):
		for team in teams:
			new_team = nflTeams(name=team.get('name'), nfl_profile_link=team.get('nfl_profile_link'), instagram_link=team.get('instagram_link'))
			if not nflTeams.objects.filter(name=new_team.name).exists():
				new_team.save()
			else:
				print("Everything is ok with {}".format(new_team.get('name')))




