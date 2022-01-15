from django.shortcuts import render
from users.forms import TeamForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
	if request.method=="POST":
		form=TeamForm(request.POST)
		if (form.is_valid):
			#Check for Redundant Roll Numbers
			form.save()
			return HttpResponseRedirect('/')

	else:
		form=TeamForm()

	
	return render(request,'game/sarcasmbase.html')