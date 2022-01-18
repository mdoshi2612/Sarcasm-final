from django.shortcuts import render
from .models import Team
from users.forms import TeamForm
from django.http import HttpResponseRedirect
from .models import Team

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

def leaderboard(request):
    return render(request,'users/leaderboard.html')