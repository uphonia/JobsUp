from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate

from .forms import UserForm
from .models import User

# Create your views here.
@csrf_exempt
def index(request):
	return render(request, 'index.html')

def sign_up(request):
	if request.method = 'GET':
		form = UserForm(request.GET)

		context = ''
        template = ''

		if form.is_valid():
			user = {}
			if form.cleaned_data["user"] == "Company":
				user["company_name"] = form.cleaned_data["company_name"]
				
			user["first_name"] = form.cleaned_data["first_name"]
            user["last_name"] = form.cleaned_data["last_name"]
            user["email"] = form.cleaned_data["email"]
            user["password"] = form.cleaned_data["password"]
            user["area_of_interest"] = form.cleaned_data["area_of_interest"]

            user["hashid"] = str(len(user["email"] + user["password"])) + str(user["email"] + user["password"])

            u = User(** user)
            u.save()


        	if form.cleaned_data["user"] == "Company":
        		template = 'CompanyProfiles.html'
        	else:
        		template = 'UserProfiles'
        	context = {'user' : user}

    return render(request, template, context)


def log_in(request):
	template = ""
	if request.method = 'GET':
		form = LogIn(request.GET)
		if form.is_valid():
			user = authenticate(form.cleaned_data["email"], form.cleaned_data["password"])
			if(user is not None):
				template = "authenticated"
				return HttpResponseRedirect("profile page placeholder") #redirect if login is good
	return render(request, "Some Error Message Html Page", "Context")


def edit_Profile(request):


