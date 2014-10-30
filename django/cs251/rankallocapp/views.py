from django.shortcuts import render
from django.http import HttpResponse
from rankallocapp.models import Candidate 
# Create your views here.

def main(request):
	return render(request,'home.html')

def register(request):
	errors = []
	if request.method == 'POST':
		if not request.POST.get('roll', ''):
			errors.append('Enter your Roll Number',)
		if not request.POST.get('passkey', ''):
			errors.append('Enter your passkey',)
		if not request.POST.get('passwd',''):
			errors.append('Enter the password',)
		if not request.POST.get('passwd',) == request.POST.get('cpasswd',):
			errors.append('The password fields do not match. Try Again.',)
		if not errors:
			my_cand = Candidate(roll=request.POST.get('roll', '') ,passwd = request.POST.get('passwd', ''),passkey = request.POST.get('passkey', ''))
			my_cand.save()
			#add to database



			return render(request, 'home.html')
	return render(request, 'register.html',
		{'errors': errors})