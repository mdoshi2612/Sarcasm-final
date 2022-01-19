from pyexpat import model
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Level(models.Model):
	""" A model representing a single level """
	DEFAULT_LEVEL = 1
	level_id = models.IntegerField(primary_key=True) 
	title = models.CharField(max_length=100)
	question = models.CharField(max_length=1000, blank = True)
	answer = models.CharField(max_length=120)
	image = models.ImageField(upload_to = 'static', null = True,	blank = True)
	audiofile= models.FileField(upload_to='static/', null=True, blank = True, verbose_name="")
	videofile= models.FileField(upload_to='static/', null=True, blank = True, verbose_name="")

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
	points=models.IntegerField(default=0, null=True)
	current_level = models.ForeignKey(Level, default=Level.DEFAULT_LEVEL, on_delete=models.CASCADE, null=True,)
	current_level_time = models.DateTimeField(default=timezone.now, null=True)
	# username = models.CharField(max_length=100, null=True, blank = True)
	# password = models.CharField(max_length=100, null=True, blank = True)
	user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
	# score = models.IntegerField(default=0)
	bonus_attempted = models.IntegerField(default=0)
	bonus_level_id = models.IntegerField(default=1)

class BonusQuestion(models.Model):
	# question = RichTextField(config_name = 'awesome_ckeditor', blank = True)
	DEFAULT_LEVEL = 1

	level_id = models.IntegerField(primary_key=True) 
	question = models.CharField(max_length=1000, blank = True)
	answer = models.CharField(max_length=120)
	expiration_date = models.DateTimeField()
	live_date = models.DateTimeField()

	image = models.ImageField(upload_to = 'static', null = True,	blank = True)
	audiofile= models.FileField(upload_to='static/', null=True, blank = True, verbose_name="")
	videofile= models.FileField(upload_to='static/', null=True, blank = True, verbose_name="")
	title = models.CharField(max_length=100)
