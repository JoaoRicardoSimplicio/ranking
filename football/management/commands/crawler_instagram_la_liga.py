from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import requests
import json

from overall.models import Team

from overall.instagram import get_instagram_information, save_instagram_information


class Command(BaseCommand):
    help = """
        You can use this command to extract information from instagram of teams. 
	 	But first, you need to run the command crawler_nfl.
    """

    def handle(self, *args, **kwargs):
        self.teamsList = Team.objects.filter(sport='football', country='spain')
        self.teamsInstagramList = get_instagram_information(self.teamsList)
        save_instagram_information(self.teamsInstagramList)