from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout

from .forms import SignUpForm, LogInForm, ProfileForm, MapRequestForm
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
	temp = 0
	template = ""
	if request.method == 'POST':
		form = ProfileForm(request.POST)
		if form.is_valid():
			u = Company.objects.filter(hashid = form.cleaned_data['hashid'])
			if(len(u) == 0):
				temp = 1
				u = User.objects.filter(hashid = form.cleaned_data['hashid'])
			u = u[0]
			print('Address' + form.cleaned_data['address'])
			if temp == 0:
				template = "CompanyProfiles.html"
				if u.profile is None:
					cprof = Profile(company_name = form.cleaned_data['company_name'],
						website = form.cleaned_data['website'], phone_num = form.cleaned_data['phone_num']
						, address = form.cleaned_data['address'])
					cprof.save()
					setattr(u, 'profile', cprof)
				else:
					setattr(u.profile, 'company_name', form.cleaned_data['company_name'])
					setattr(u.profile, 'website', form.cleaned_data['website'])
					setattr(u.profile, 'phone_num', form.cleaned_data['phone_num'])
					setattr(u.profile, 'address', form.cleaned_data['address'])
					u.profile.save()
				#u.profile = cprof
			elif temp == 1:
				template = "UserProfiles.html"
				if u.profile is None:
					uprof = Profile(degree = form.cleaned_data['degree'],
						resume = form.cleaned_data['resume'], phone_num = form.cleaned_data['phone_num'],
						address = form.cleaned_data['address'])
					uprof.save()
					u.profile = uprof
				else:
					setattr(u.profile, 'degree', form.cleaned_data['degree'])
					setattr(u.profile, 'resume', form.cleaned_data['resume'])
					setattr(u.profile, 'phone_num', form.cleaned_data['phone_num'])
					setattr(u.profile, 'address', form.cleaned_data['address'])
					u.profile.save()
				setattr(u, 'first_name', form.cleaned_data['first_name'])
				setattr(u, 'last_name', form.cleaned_data['last_name'])
			setattr(u, 'email', form.cleaned_data['email'])

			u.save();

			return render(request, template, {'user':u})
	return redirect('/')

def view_map(request):
	if request.method == 'GET':
		user = {}
		comp = {}
		radius = ''
		form = MapRequestForm(request.GET)
		if form.is_valid():
			user = User.objects.filter(hashid = form.cleaned_data['hashid'])
			user = user[0]

			r = form.cleaned_data['radius']
			radius = ''.join(x for x in r if x.isdigit())
			comp = Company.objects.all()


	context = {'user': user, 'company': comp, 'radius':radius}
	return render(request, "Map.html", context)
