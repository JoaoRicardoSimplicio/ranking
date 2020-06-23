from django.urls import path
from . import views

urlpatterns = [
	path('teams/', views.AllNflTeams.as_view(), name='all_nfl_teams'),
	# path('teams_instagrams/', views.AllTeamsInstagrams.as_view(), name='all_teams_instagrams')
]
