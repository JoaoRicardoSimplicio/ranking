from tqdm import tqdm
from .models import Team


def save_teams(teamsList, **kwargs):
	print("step 2: Save all teams...")
	for team in tqdm(teamsList):
		newTeam = Team(
			name=team.get('name'),
			site_profile_link=team.get('site_profile_link'), 
			instagram_link=team.get('instagram_link'),
			sport=team.get('sport'),
			country=team.get('country')
        )
		if Team.objects.filter(name=newTeam.name).exists() is False and kwargs.get('refresh') is not True:
			newTeam.save()
		elif Team.objects.filter(name=newTeam.name).exists() is True and kwargs.get('refresh') is True:
			previousInstanceTeam = Team.objects.get(name=newTeam.name)
			previousInstanceTeam.name = newTeam.name
			previousInstanceTeam.site_profile_link = newTeam.site_profile_link
			previousInstanceTeam.instagram_link = newTeam.instagram_link
			previousInstanceTeam.country = newTeam.country
			previousInstanceTeam.sport = newTeam.sport
			previousInstanceTeam.save()
		elif Team.objects.filter(name=newTeam.name).exists() is False and kwargs.get('refresh') is True:
			newTeam.save()