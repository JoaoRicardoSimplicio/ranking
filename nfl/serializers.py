from rest_framework import serializers
from nfl.models import nflTeams, nflInstagrams


class NflInstagramSerializer(serializers.ModelSerializer):
	class Meta:
		model = nflInstagrams
		fields = ('username', 'followers', 'followings', 'profile_picture')


class NflTeamsSerializer(serializers.ModelSerializer):
	instagram = NflInstagramSerializer(many=True, read_only=True)
	class Meta:
		model = nflTeams
		fields = ('name', 'nfl_profile_link', 'instagram')
