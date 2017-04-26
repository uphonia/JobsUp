from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

from .forms import SignUpForm, LogInForm, ProfileForm
from .models import Profile, Company, User, Application

# Create your views here.
@csrf_exempt
def index(request):
	return render(request, 'index.html')

def sign_up(request):
	template = ''
	u = {}
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		print(form.errors)
		if form.is_valid():
			user = {}
			user['username'] = form.cleaned_data['username']
			user['first_name'] = form.cleaned_data['first_name']
			user['last_name'] = form.cleaned_data['last_name']
			user['email'] = form.cleaned_data['email']
			user['password'] = form.cleaned_data['password']
			if form.cleaned_data['personnel'] == 'Company':
				user['hashid'] = str(len(user['username'] + user['password'])) + str(user['username'] + user['password'])
				template = 'CompanyProfiles.html'
				query = Company.objects.filter(hashid = user['hashid'])
				if len(query) == 0:
					u = Company(** user)
					u.save()
				else:
					return redirect('/')
			elif form.cleaned_data['personnel'] == 'Employee':
				user['hashid'] = str(len(user['username'] + user['password'])) + str(user['username'] + user['password'])
				template = 'UserProfiles.html'
				query = User.objects.filter(hashid = user['hashid'])
				if len(query) == 0:
					u = User(** user)
					u.save()
				else:
					return redirect('index')
			return render(request, template, {'user':u})
	else:
		form = SignUpForm()
	return redirect('index')

def log_in(request):
	template = ""
	if request.method == 'GET':
		form = LogInForm(request.GET)
		print(form.errors)
		if form.is_valid():
			u = Company.objects.filter(hashid = str(len(form.cleaned_data['username'] + form.cleaned_data['password'])) + str(form.cleaned_data['username'] + form.cleaned_data['password']))
			if(len(u) == 0):
				u = User.objects.filter(hashid = str(len(form.cleaned_data['username'] + form.cleaned_data['password'])) + str(form.cleaned_data['username'] + form.cleaned_data['password']))
				if(len(u) == 0):
					return redirect('index')
				else:
					template = "UserProfiles.html"
			else:
				template = "CompanyProfiles.html"
			u = u[0]
			return render(request, template, {'user':u})
	return redirect('index')

def log_out(request):
	return redirect('index')

def edit_profile(request):
	if request.method == 'POST':
		form = ProfileForm(request.POST)
