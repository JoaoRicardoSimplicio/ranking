from django.shortcuts import render
from rest_framework import generics


from .models import nflTeams, nflInstagrams
from nfl.serializers import NflTeamsSerializer, NflInstagramSerializer



class AllNflTeams(generics.ListAPIView):
	queryset = nflTeams.objects.all()
	serializer_class = NflTeamsSerializer


	
