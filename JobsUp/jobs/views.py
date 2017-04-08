from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
@csrf_exempt
def index(request):
	return render(request, 'index.html')