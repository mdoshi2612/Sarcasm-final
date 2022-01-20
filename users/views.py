from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Team, Level, BonusQuestion
from users.forms import TeamForm
from django.http import HttpResponseRedirect
from .models import Team, Level
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
import math
import random
from django.core.mail import send_mail, BadHeaderError
from .forms import LevelForm
from django.urls import reverse
from django.views import View
from django.utils import timezone

# Create your views here.

def home(request):
	error_message = ""
	context = {'error_message':error_message}
	if request.method=="POST":
		
		team_name = request.POST.get('team_name')
		leader_first_name = request.POST.get('leader_first_name')
		leader_last_name = request.POST.get('leader_last_name')
		leader_roll_number = request.POST.get('leader_roll_number')
		leader_whatsapp_number = request.POST.get('leader_whatsapp_number')
		team_logo = request.POST.get('team_logo')
		player2_first_name = request.POST.get('player2_first_name')
		player2_last_name = request.POST.get('player2_last_name')
		player2_roll_number = request.POST.get('player2_roll_number')
		player3_first_name = request.POST.get('player3_first_name')
		player3_last_name = request.POST.get('player3_last_name')
		player3_roll_number = request.POST.get('player3_roll_number')
		player4_first_name = request.POST.get('player4_first_name')
		player4_last_name = request.POST.get('player4_last_name')
		player4_roll_number = request.POST.get('player4_roll_number')
		player5_first_name = request.POST.get('player5_first_name')
		player5_last_name = request.POST.get('player5_last_name')
		player5_roll_number = request.POST.get('player5_roll_number')
		league = request.POST.get('league')

		allowed_roll_numbers = ["21",""]
		if league=="Freshies Only" and (leader_roll_number[:2] not in allowed_roll_numbers or player2_roll_number[:2] not in allowed_roll_numbers or player3_roll_number[:2] not in allowed_roll_numbers or player4_roll_number[:2] not in allowed_roll_numbers or player5_roll_number[:2] not in allowed_roll_numbers):
			error_message = "Please register for open category"
			context = {'error_message':error_message}
			return render(request,'users/sarcasmbase.html', context)

			
		team = Team(team_name = team_name, leader_first_name = leader_first_name, leader_last_name = leader_last_name,
		leader_roll_number = leader_roll_number, leader_whatsapp_number = leader_whatsapp_number, team_logo = team_logo,
		player2_first_name = player2_first_name, player2_last_name = player2_last_name, player2_roll_number = player2_roll_number,
		player3_first_name = player3_first_name, player3_last_name = player3_last_name, player3_roll_number = player3_roll_number,
		player4_first_name = player4_first_name, player4_last_name = player4_last_name, player4_roll_number = player4_roll_number,
		player5_first_name = player5_first_name, player5_last_name = player5_last_name, player5_roll_number = player5_roll_number,
		league = league)


		
		team.save()
		success = True
		context = {'success':success}
	
	return render(request,'users/sarcasmbase.html', context)


def faq(request):
    return render(request,'users/faq.html')

def ourteam(request):
    return render(request,'users/ourteam.html')

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
    recipient = [email]
    send_mail(subject, message, email_from, recipient, fail_silently=True)
    return None

def generatepassword(request):
	if request.method == 'POST':
		leader_roll_number=request.POST.get('leader_roll_number')
		team = Team.objects.filter(leader_roll_number=leader_roll_number).first()
		if team is None:
				context = {'message': 'Team not found', 'class': 'danger'}
				return render(request, 'users/generatepassword.html', context)
		else:
			# username=request.POST.get('username')
			email=request.POST.get('email')
			password = User.objects.make_random_password()
			user = User.objects.create(username = leader_roll_number, email = email)
			user.set_password(password)
			team.user = user
			user.save()
			team.save()
			send_otp(email, password) 		
			return redirect('login')
			
		
	return render(request, 'users/generatepassword.html')
    
		
		



def login1(request):
	if request.method == 'POST':
		uname=request.POST.get('username')
		password=request.POST.get('password')
		user = User.objects.filter(username=uname).first()
		if user is None:
			context = {'message': 'Username does not exist', 'class': 'danger'}
			return render(request, 'users/login.html', context)
		else:
			team = Team.objects.filter(user=user).first()
			user2 = authenticate(request, username=uname, password=password)
			if user2 is not None:
				login(request, user2)
				return redirect(reverse('play'))
			else:
				context = {'message': 'Incorrect password', 'class': 'danger', 'user2': user.password, 'pass': password}
				return render(request, 'users/login.html', context)
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

		
		cur_user = Team.objects.get(user=request.user)
		cur_level = cur_user.current_level	
		# cur_level = Level.objects.get(level_id=1)
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
		cur_user = Team.objects.get(user=request.user)
		cur_level = cur_user.current_level
		level_number = cur_user.current_level.level_id

		form = self.form_class(request.POST)    #What if request != 'POST' ????
		if form.is_valid():
			ans = form.cleaned_data.get('answer')
			if ans == cur_level.answer:
				level_number = cur_user.current_level.level_id
				try:
					cur_user.current_level = Level.objects.get(level_id = level_number + 1)
					cur_user.points=cur_user.points+3
					# cur_user.current_level_time = timezone.now()	 					
					cur_user.save()
				except:
					pass

		return redirect(reverse('play'))

class Bonus(View) :
	# Form field for the level
	form_class = LevelForm

	def get(self, request, *args, **kwargs):
		cur_user = Team.objects.get(user=request.user)
		try:
			bonus_level = BonusQuestion.objects.get(level_id=cur_user.bonus_level_id)
			livedatetime=bonus_level.live_date
			# print("live date ", livedatetime)
			current_time=timezone.now()
			# print("current time ",current_time)
			expdatetime = bonus_level.expiration_date
			# print("expiry date ",expdatetime)
			expired = bonus_level.expiration_date < current_time
			if expired:
				# print("The question has expired")
				bonus_array = BonusQuestion.objects.filter(level_id__gt=cur_user.bonus_level_id)
				# print(bonus_array)
				for q in bonus_array:
					if q.live_date < current_time and current_time<q.expiration_date:
						cur_user.bonus_level_id = q.level_id
						# print("The bonus id is ",cur_user.player.bonus_level_id)
						bonus_level = BonusQuestion.objects.get(level_id=cur_user.bonus_level_id)
						cur_user.save()

			if bonus_level.expiration_date<timezone.now() or bonus_level.live_date>timezone.now():
				print("Question {0} not live".format(bonus_level.level_id))
				raise
		except:
			print("Error")
			return redirect(reverse('play'))
		form = self.form_class

		question = bonus_level.question
		livedatetime = bonus_level.live_date
		expdatetime = bonus_level.expiration_date
	
		current_time = timezone.now()
		year = expdatetime.strftime('%Y')
		month = expdatetime.strftime('%m')
		day = expdatetime.strftime('%d')
		hour = expdatetime.strftime('%H')
		minute = expdatetime.strftime('%M')
		second = expdatetime.strftime('%S')

		context = {'question': question,'year': year,'month': month,'day': day,'hour': hour,'minute': minute,
			'second':second,'expdate': expdatetime,'livedate': livedatetime,'now': current_time,'form':form,}
		return render(request, 'users/bonus.html', context)
	

	def post(self,request, *args, **kwargs):
		"""
		POST request
		1. Get the current user and their answer
		2. If the answer is correct, update the level
		"""
		cur_user = Team.objects.get(user=request.user)
		bonus_level = BonusQuestion.objects.get(level_id=cur_user.bonus_level_id)
		form = self.form_class(request.POST)    #What if request != 'POST' ????
		if form.is_valid():
			ans = form.cleaned_data.get('answer')
			if ans == bonus_level.answer:
				
				level_number = bonus_level.level_id
				if cur_user.bonus_level_id == level_number:
					try:
						cur_user.bonus_level_id += 1
						cur_user.bonus_attempted=cur_user.bonus_attempted+1
						cur_user.points += 5	 					
						cur_user.save()
						return redirect(reverse('play'))
					except:
						pass
				else:
					print("Cant play Bonus Twice")
					return redirect(reverse('play'))
			else:
				print("Wrong Answer! Try Again")
				return redirect(reverse('bonus'))
		return redirect(reverse('play'))

		
def leaderboard(request):
	top_teams = Team.objects.order_by('-points')[:10]
	context = {'top_teams': top_teams}
	return render(request,'users/leaderboard.html', context)
