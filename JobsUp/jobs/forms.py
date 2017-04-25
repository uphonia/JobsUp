from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Profile


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length = 200, required = False)
	last_name = forms.CharField(max_Length = 200, required = False)
	email = forms.EmailField(max_length = 254, help_text = 'Required. Inform a valid email address.')

	class Meta:
		model = User
			fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('url')