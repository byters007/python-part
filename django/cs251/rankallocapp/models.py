from django.db import models
from django import forms

# Create your models here.
#class myCandidate(models.Model):

class Programme(forms.ModelForm):
	name = forms.CharField()

class Candidate(forms.modelsForm):
	roll = forms.CharField(max_length=10,min_length=10)
	passwd = forms.CharField(widget=forms.PasswordInput())
	passkey = forms.CharField()
	#rank = forms.PositiveIntegerField()
	#choices= forms.ManyToManyField(Programme)
	#remaining = fomrs.ManyToManyField(Programme)
