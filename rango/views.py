from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hey there partner!\nCheck out <a href='/rango/about/'>About</a>")

def about(request):
	return HttpResponse("Rango says here is the about page.\nCheck out <a href='/rango/'>Index</a>")
