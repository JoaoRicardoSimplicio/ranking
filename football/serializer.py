from rest_framework import serializers
from overall.models import Team, Instagram


class InstagramSerializer(serializers.ModelSerializer):
	class Meta:
		model = Instagram
		fields = ('username', 'followers', 'followings', 'profile_picture')


class TeamsSerializer(serializers.ModelSerializer):
	instagram = InstagramSerializer(many=True, read_only=True)
	class Meta:
		model = Team
		fields = ('name', 'site_profile_link', 'instagram_link', 'sport', 'country', 'instagram')

