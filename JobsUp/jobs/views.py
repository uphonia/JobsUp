from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

from .forms import UserForm,  SignUpForm, LogInForm
from .models import Profile

# Create your views here.
@csrf_exempt
def index(request):
	return render(request, 'index.html')

def sign_up(request):
	template = ''
	print('Begin')
	if request.method == 'POST':
		print('GOD')
		form = SignUpForm(request.POST)
		print(form.errors)
		if form.is_valid():
			print('HERE')
			user = {}
			user['username'] = form.cleaned_data['username']
			user['first_name'] = form.cleaned_data['first_name']
			user['last_name'] = form.cleaned_data['last_name']
			user['email'] = form.cleaned_data['email']
			user['password'] = form.cleaned_data['password']
			user['personnel'] = form.cleaned_data['personnel']
			user['hashid'] = str(len(user['username'] + user['password'] + user['email'])) + str(user['username'] + user['password'])
			if user['personnel'] == 'Company':
				template = 'CompanyProfiles.html'
			elif user['personnel'] == 'Employee':
				template = 'UserProfiles.html'

			query = Profile.objects.filter(hashid = user['hashid'])
			if len(query) == 0:
				u = Profile(** user)
				u.save()
			else:
				return redirect('/')
			return render(request, template, {'user':u})
	else:
		form = SignUpForm()
	print('END')
	return redirect('/')

def log_in(request):
	if request.method == 'GET':
		form = LogInForm(request.GET)
		print(request.GET)
		if form.is_valid():
			u = Profile.objects.filter(hashid = str(len(form.cleaned_data['username'] + form.cleaned_data['password'] + form.cleaned_data['email'])) + str(form.cleaned_data['username'] + form.cleaned_data['password']))
			if(len(u) == 0):
				return redirect('index')
			u = u[0]
			if u.personnel == 'Company':
				return render(request, 'CompanyProfiles.html', {'user':u})
			elif u.personnel == 'Employee':
				return render(request, 'UserProfiles.html', {'user':u})
	return redirect('index')

#def log_out(request):
	

#def edit_Profile(request):