from django.db import models

# Create your models here.
class Team(models.Model):
	leader_name = models.CharField(max_length=100)
	leader_roll_number = models.CharField(max_length=100, primary_key=True)
	year_of_study = models.CharField(max_length=100)
	team_name = models.CharField(max_length=100)
	team_logo = models.CharField(max_length=100, null=True)
	player1 = models.CharField(max_length=100)
	player2 = models.CharField(max_length=100)
	player3 = models.CharField(max_length=100)
	player4 = models.CharField(max_length=100)
	score = models.IntegerField(default=0)
