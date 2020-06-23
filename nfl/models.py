from django.db import models

# Create your models here.

class nflTeams(models.Model):
	name = models.CharField(max_length=100, unique=True, null=False)
	instagram_link = models.URLField(max_length=200, null=True)
	nfl_profile_link = models.URLField(max_length=200, null=True)
	
	class Meta:
		ordering = ['-instagram__followers']

	def __str__(self):
		return self.name



class nflInstagrams(models.Model):
	team = models.ForeignKey(nflTeams, on_delete=models.CASCADE, related_name='instagram')
	followers = models.IntegerField(null=True)
	followings = models.IntegerField(null=True)
	username = models.CharField(max_length=50, unique=True)
	profile_picture = models.URLField(max_length=200, null=False)
	profile_verifyed = models.BooleanField()

	class Meta:
		ordering = ['-followers']

	def __str__(self):
		return self.username
