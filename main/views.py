from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
	return HttpResponse("Wow this knocks my <strong>socks</strong> off")