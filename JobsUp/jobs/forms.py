from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
	username = forms.CharField(max_length = 200, required = True)
	first_name = forms.CharField(max_length = 200, required = True)
	last_name = forms.CharField(max_length = 200, required = True)
	email = forms.EmailField(max_length = 254, required = True)
	password = forms.CharField(max_length = 200, required = True)
	personnel = forms.CharField(max_length = 200, required = True)

class LogInForm(forms.Form):
	username = forms.CharField(max_length = 200, required = True)
	password = forms.CharField(max_length = 200, required = True)

class ProfileForm(forms.Form):
	hashid = forms.CharField(max_length = 200, required = True)
