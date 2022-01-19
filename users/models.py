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
	team_name = models.CharField(max_length=100, blank=False)
	leader_first_name = models.CharField(max_length=100, blank=False)
	leader_last_name = models.CharField(max_length=100, blank=False)
	leader_roll_number = models.CharField(max_length=100, primary_key=True, blank=False)
	leader_whatsapp_number = models.CharField(max_length=100, blank=False)	
	team_logo = models.CharField(max_length=100, null=True, blank=False)
	player2_first_name = models.CharField(max_length=100, blank = True)
	player2_last_name = models.CharField(max_length=100, blank = True)
	player2_roll_number = models.CharField(max_length=100, blank = True)
	player3_first_name = models.CharField(max_length=100, blank = True)
	player3_last_name = models.CharField(max_length=100, blank = True)
	player3_roll_number = models.CharField(max_length=100, blank = True)
	player4_first_name = models.CharField(max_length=100, blank = True)
	player4_last_name = models.CharField(max_length=100, blank = True)
	player4_roll_number = models.CharField(max_length=100, blank = True)
	player5_first_name = models.CharField(max_length=100, blank = True)
	player5_last_name = models.CharField(max_length=100, blank = True)
	player5_roll_number = models.CharField(max_length=100, blank = True)
	points=models.IntegerField(default=0, null=True)
	current_level = models.ForeignKey(Level, default=Level.DEFAULT_LEVEL, on_delete=models.CASCADE, null=True,)
	current_level_time = models.DateTimeField(default=timezone.now, null=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
	freshies_only = models.BooleanField(default=0)
	open = models.BooleanField(default=0)