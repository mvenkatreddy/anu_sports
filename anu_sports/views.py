from django.template import RequestContext
from django.shortcuts import render_to_response, render

def home(request):
	context = RequestContext(request)
	return render_to_response("home.html", {}, context)


def brand(request):
	context = RequestContext(request)
	return render_to_response("index.html", {}, context)
