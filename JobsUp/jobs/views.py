from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers

from .forms import SignUpForm, LogInForm, ProfileForm, MapRequestForm
from .models import Company, Individual, Application

import json
from django.core import serializers

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
					u = Individual(** user)
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
				u = Individual.objects.filter(hashid = str(len(form.cleaned_data['username'] + form.cleaned_data['password'])) + str(form.cleaned_data['username'] + form.cleaned_data['password']))
				if(len(u) == 0):
					return redirect('index')
				else:
					template = "UserProfiles.html"
			else:
				template = "CompanyProfiles.html"
			u = u[0]
			print(u.hashid)
			return render(request, template, {'user':u})
	return redirect('index')

def log_out(request):
	return redirect('index')

def edit_profile(request):
	temp = 0
	u = {}
	template = ""
	if request.method == 'POST':
		form = ProfileForm(request.POST)
		print(form)
		print ("\n")
		if form.is_valid():
			try:
				print(form.cleaned_data['hashid'])
				print("\n")
				u = Company.objects.filter(hashid = form.cleaned_data['hashid'])
			except Company.DoesNotExist:
				u = None
				return redirect('/')
			if(len(u) == 0):
				temp = 1
				try:
					u = Individual.objects.filter(hashid = form.cleaned_data['hashid'])
				except Individual.DoesNotExist:
					u = None
					return redirect('/')
			u = u[0]
			if temp == 0:
				template = "CompanyProfiles.html"
				setattr(u, 'company_name', form.cleaned_data['company_name'])
				setattr(u, 'website', form.cleaned_data['website'])
				setattr(u, 'phone_num', form.cleaned_data['phone_num'])
			elif temp == 1:
				template = "UserProfiles.html"
				setattr(u, 'degree', form.cleaned_data['degree'])
				setattr(u, 'resume', form.cleaned_data['resume'])
				setattr(u, 'phone_num', form.cleaned_data['phone_num'])
				setattr(u, 'first_name', form.cleaned_data['first_name'])
				setattr(u, 'last_name', form.cleaned_data['last_name'])

			setattr(u, 'email', form.cleaned_data['email'])
			setattr(u, 'str_address', form.cleaned_data['str_address'])
			setattr(u, 'city', form.cleaned_data['city'])
			setattr(u, 'state', form.cleaned_data['state'])
			setattr(u, 'zipcode', form.cleaned_data['zipcode'])

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
			user = Individual.objects.filter(hashid = form.cleaned_data['hashid'])
			user = user[0]

			r = form.cleaned_data['radius']
			radius = ''.join(x for x in r if x.isdigit())
			comp = Company.objects.all()
			

	company = []
	length = 0
	#company = serializers.serialize('json', comp)
	for c in comp:
		company.insert(0, comp[length])
		length = length+1
	context = {'user': user, 'company': company, 'radius':radius}
	#json_context = json.dumps(context)
	return render(request, "Map.html", context)

# for viewing profile from map
def view_profile(request):
    if request.method == 'GET':
        user = {}
        form = ProfileForm(request.GET)
        if form.is_valid():
            user = Individual.objects.filter(hashid = form.cleaned_data['hashid'])
            user = user[0]
            
    context = {'user': user}
    return render(request, "UserProfiles.html", context)
    
def showCompanies(request):
    companies = Company.objects.all()
    return render_to_response('Map.html', {"companies": companies})
    
def showCompDetail(request, comp_id):
    companies = Company.objects.get(id=comp_id)
    return render_to_response('Map.html', {"companies": companies})
    
    
