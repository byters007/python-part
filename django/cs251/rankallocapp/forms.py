from django import forms

class RegistrationForm(forms.Form):
    roll = forms.CharField(label='Roll Number', max_length = 10, min_length = 10)
    passkey = forms.CharField(label = 'Pass Key')
    passwd = forms.CharField(label = 'Password')
    cpasswd = forms.CharField(label = 'Confirm Password')

class LoginForm(forms.Form) :
	roll = forms.CharField(label='Roll Number', max_length = 10, min_length = 10)
	passwd = forms.CharField(label = 'Password')