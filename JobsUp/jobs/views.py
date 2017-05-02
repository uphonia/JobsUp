from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from django.core.mail import send_mail

from .forms import SignUpForm, LogInForm, ProfileForm, MapRequestForm, ViewApplicationForm
from .models import Company, Individual, Application

from geopy.geocoders import Nominatim
from geopy.distance import vincenty

import geocoder
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

def post_job(request):
	if request.method == 'POST':
		company = Company.objects.get(hashid = request.POST.get("hashid", ""))
		company.job_post = request.POST.get("job", "")
		company.save()
	return render(request,'CompanyProfiles.html', {'user': company})

def view_map(request):
	freegeoip = "http://freegeoip.net/json"
	if request.method == 'GET':
		geolocator = Nominatim()
		user = {}
		comp = {}
		r = 0
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
	current = geocoder.ip('me')
	for c in comp:
		add = c.str_address + " " + c.city + ", " + c.state + " " + c.zipcode;
		location = geocoder.google(add)
		if vincenty(location.latlng, current.latlng).miles < int(r) and c.job_post != "":
			company.insert(length, c)
			length = length+1
	context = {'user': user, 'company': company, 'radius':radius}
	#json_context = json.dumps(context)
	return render(request, "Map.html", context)

# for viewing profile from map
def view_profile(request):
    if request.method == 'GET':
        user = {}
        user = Individual.objects.filter(hashid = request.GET.get("hashid"))
        user = user[0]
            
    context = {'user': user}
    return render(request, "UserProfiles.html", context)

def view_c_profile(request):
    if request.method == 'GET':
        user = {}
        user = Company.objects.filter(hashid = request.GET.get("hashid"))
        user = user[0]
            
    context = {'user': user}
    return render(request, "CompanyProfiles.html", context)
    
def showCompanies(request):
    companies = Company.objects.all()
    return render_to_response('Map.html', {"companies": companies})
    
def showCompDetail(request, comp_id):
    companies = Company.objects.get(id=comp_id)
    return render_to_response('Map.html', {"companies": companies})

def submit_application(request):
	j = {}
	if request.method == 'GET':
		job_real = {}
		user = Individual.objects.get(hashid = request.GET.get("ihashid", ""))
		comp = Company.objects.get(hashid = request.GET.get("chashid", ""))
		job_real['applicant'] = user
		job_real['company'] = comp
		query = Application.objects.filter(applicant = user, company = comp)
		if len(query) == 0:
			j = Application(** job_real)
			j.save()
	return render(request, 'UserProfiles.html', {'user':user})

def view_applicants(request):
	applicants = []
	length = 0
	context = {}
	if request.method == 'GET':
		form = ViewApplicationForm(request.GET)
		if form.is_valid():
			comp = Company.objects.get(hashid = form.cleaned_data['hashid'])
			applications = Application.objects.filter(company = comp)
			for a in applications:
				u = Individual.objects.get(hashid = a.applicant.hashid)
				applicants.insert(length, u)
				length = length+1
			context = {'company':comp, 'applicants':applicants}
	return render(request, 'Applicants.html', context)
    
def company_response(request):
	applicants = []
	comp = {}
	length = 0
	context = {}
	if request.method == 'GET':
		comp = Company.objects.get(hashid = request.GET.get("chashid"))
		applicant = Individual.objects.get(hashid = request.GET.get("ihashid"))
		application = Application.objects.get(company = comp, applicant = applicant)
		application.delete()
		if 'Accept' in request.GET:
			send_mail('Application Accepted', comp.company_name + ' has accepted your application', 'tier3tier@gmail.com', [applicant.email], fail_silently = False,)
		elif 'Decline' in request.GET:
			send_mail('Application Denied', comp.company_name + ' has declined your application', 'tier3tier@gmail.com', [applicant.email], fail_silently = False,)
		applications = Application.objects.filter(company = comp)
		for a in applications:
			u = Individual.objects.get(hashid = a.applicant.hashid)
			applicants.insert(length, u)
			length = length+1
		context = {'company':comp, 'applicants':applicants}
	return render(request, 'Applicants.html', context)