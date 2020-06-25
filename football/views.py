from django.shortcuts import render
from rest_framework import generics

from overall.models import Team
from football.serializer import TeamsSerializer


class PremierLeagueTeams(generics.ListAPIView):
	queryset = Team.objects.filter(sport='football', country='england')
	serializer_class = TeamsSerializer


class LaLigaTeams(generics.ListAPIView):
	queryset = Team.objects.filter(sport='football', country='spain')
	serializer_class = TeamsSerializer


class TenMostFamousTeams(generics.ListAPIView):
	queryset = Team.objects.filter(sport='football')[:10]
	serializer_class = TeamsSerializer
