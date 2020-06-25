from django.urls import path
from . import views

urlpatterns = [
    path('premier_league/teams/', views.PremierLeagueTeams.as_view(), name='premier_league_teams'),
    path('la_liga/teams/', views.LaLigaTeams.as_view(), name='la_liga_teams'),
    path('top10/teams/', views.TenMostFamousTeams.as_view(), name='ten_most_famous_teams')
]