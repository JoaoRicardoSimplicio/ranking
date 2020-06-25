from django.shortcuts import render
from rest_framework import generics

from overall.models import Team
from overall.serializer import TeamsSerializer

class TenMostFamousInstagrams(generics.ListAPIView):
    queryset = Team.objects.all()[:10]
    serializer_class = TeamsSerializer