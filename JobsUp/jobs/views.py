from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.contenttypes import contenttypes

from .forms import UserForm,  SignUpForm, ProfileForm
from .models import Profile

# Create your views here.
@csrf_exempt
def index(request):
	return render(request, 'index.html')

def sign_up(request):
	template = ''
	if request.method == 'POST':
		form = SignUpForm(request.GET)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.company_name = form.cleaned_data.get('company_name')
			if form.cleaned_data['personnel'] == 'Company':
				user.profile.corpse = 1
				template = 'CompanyProfiles.html'
			elif form.cleaned_data['personnel'] == 'Employee':
				user.profile.corpse = 0
				template = 'UserProfiles.html'
			user.save()
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username = user.username, password = raw_password)
			login(request, user)
			return render(request, template, {'user':user})
	else:
		form = SignUpForm()
	return render(request, 'index.html')

def log_in(request):
	username = request.GET['user_log_in']
	password = request.GET['pass_log_in']
	user = authenticate(request, username = username, password = password)
	if user is not None:
		login(request, user)
		if user.profile.corpse == 1:
			return render(request, 'CompanyProfiles.html', {'user':user})
		elif user.profile.corpse == 0:
			return render(request, 'UserProfiles.html', {'user':user})
	else
		return render(request, 'index.html')

def log_out(request):
	logout(request)
	return redirect('index')

def edit_Profile(request):

