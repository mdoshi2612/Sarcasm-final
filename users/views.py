from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Team, Level
from users.forms import TeamForm
from django.http import HttpResponseRedirect
from .models import Team
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
import math
import random
from django.core.mail import send_mail, BadHeaderError
from .forms import LevelForm
from django.urls import reverse
from django.views import View

# Create your views here.

def home(request):
	if request.method=="POST":
		leader_name = request.POST.get('leader_name')
		leader_roll_number = request.POST.get('leader_roll_number')
		year_of_study = request.POST.get('year_of_study')
		team_name = request.POST.get('team_name')
		player1 = request.POST.get('player1')
		player2 = request.POST.get('player2')
		player3 = request.POST.get('player3')
		player4 = request.POST.get('player4')
		team_logo = request.POST.get('team_logo')
		
		team = Team(leader_name=leader_name, leader_roll_number=leader_roll_number, year_of_study=year_of_study, team_name=team_name, player1=player1, player2=player2, player3=player3, player4=player4, team_logo=team_logo)
		team.save()

	
	return render(request,'users/sarcasmbase.html')


def faq(request):
    return render(request,'users/faq.html')


def generatepassword(request):
	if request.method == 'POST':
		leader_roll_number=request.POST.get('leader_roll_number')
		team = Team.objects.filter(leader_roll_number=leader_roll_number).first()
		if team is None:
				context = {'message': 'Team not found', 'class': 'danger'}
				return render(request, 'users/generatepassword.html', context)
		else:
			username=request.POST.get('username')
			email=request.POST.get('email')
			otp=generateOTP()
			user = User(username = username, email = email)
			team.username = username
			team.password = otp
			user.save()
			team.save
			send_otp(email, otp)
			return redirect('login')
			
		
	return render(request, 'users/generatepassword.html')
    
		
		

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def send_otp(email, otp_generated):
    subject = "OTP request"
    message = 'Hi, your otp is ' + str(otp_generated)
    # email_from = ('pragyaptl131996@gmail.com', 'SARC IIT Bombay')
    email_from = 'pragyaptl131996@gmail.com'
    recipient = [email, ]
    send_mail(subject, message, email_from, recipient, fail_silently=True)
    return None

def login1(request):
	if request.method == 'POST':
		uname=request.POST.get('username')
		password=request.POST.get('password')
		user = User.objects.filter(username=uname).first()
		if user is None:
			context = {'message': 'Username does not exist', 'class': 'danger'}
			return render(request, 'users/login.html', context)
		else:
			team = Team.objects.filter(username=uname).first()
			if password == team.password:
				login(request, user)
				return redirect(reverse('play'))
			else:
				context = {'message': 'Incorrect password', 'class': 'danger'}
				return render(request, 'users/login.html')
	return render(request, 'users/login.html')



class Play(View) :
	# login_url = '/login/'
	# redirect_field_name = '/register/'
	# redierct_url = '/accounts/facebook/login/callback/'
	# Form field for the level
	form_class = LevelForm


	def get(self, request, *args, **kwargs):
		""" 
		GET Request 
		1. get the current user by the request.user
		2. find their current level and return the question accordingly
		"""

		
		cur_user = Team.objects.get(username=request.user.username)
		cur_level = cur_user.current_level	
		# cur_level = Level.objects.get(level_id=5)
		form = self.form_class()
		context = {
			'level' : cur_level,
			'form': form,
		}
		return render(request,'users/play.html',context)   #{{form|crispy}} crispy form was removed try to add it back


	def post(self,request, *args, **kwargs):
		"""
		POST request
		1. Get the current user and their answer
		2. If the answer is correct, update the level
		"""
		cur_user = Team.objects.get(username=request.user.username)
		cur_level = cur_user.current_level
		level_number = cur_user.current_level.level_id

		form = self.form_class(request.POST)    #What if request != 'POST' ????
		if form.is_valid():
			ans = form.cleaned_data.get('answer')
			if ans == cur_level.answer:
				level_number = cur_user.current_level.level_id
				if level_number == 2 :
					cur_user.points=cur_user.points+3
					cur_user.current_level_time = timezone.now()	 					
					cur_user.save()
					pass
				try:
					cur_user.points=cur_user.points+3
					cur_user.current_level = Level.objects.get(level_id = level_number + 1)
					cur_user.current_level_time = timezone.now()	 					
					cur_user.save()
				except:
					pass

		return redirect(reverse('play'))

		
def leaderboard(request):
	top_teams = Team.objects.order_by('-points')[:10]
	context = {'top_teams': top_teams}
	return render(request,'users/leaderboard.html', context)
