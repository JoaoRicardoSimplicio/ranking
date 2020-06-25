from django.shortcuts import render
from rest_framework import generics

from overall.models import Team
from nfl.serializers import NflTeamsSerializer, NflInstagramSerializer


class AllNflTeams(generics.ListAPIView):
	queryset = Team.objects.filter(sport='american football')
	serializer_class = NflTeamsSerializer


	
