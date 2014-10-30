from django.shortcuts import render
from django.http import HttpResponse
from rankallocapp.models import Candidate 
# Create your views here.

def main(request) :
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid() :
			roll = form.cleaned_data['roll']
			passwd = form.cleaned_data['passwd']
			##check if such a record exists in the database
			#if(exists_in_database) :
			##	create an instance of that candidate as my_cand and pass it to session.html page
			#	return render(request , 'session.html' , {'my_cand : cand})
			#else :
			#	form = LoginForm()
			#	return render(request , 'home.html' , {'form' : form})
	else :
		form = LoginForm()
	return render(request , 'home.html' , {'form' : form})

def register(request) :
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid() :
			roll = form.cleaned_data['roll']
			passwd = form.cleaned_data['passwd']
			passkey = form.cleaned_data['passkey']
			#create a candidate and instantiate
			my_cand = Candidate(roll , passwd , passkey)
			my_cand.save()
			return HttpResponse('/home')
	else :
		form = RegistrationForm()
	return render(request , 'register.html' , {'form' : form})