from django.http.request import host_validation_re
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json
# urllib.request to make a request to api
import urllib.request
from . models import Automate_Email




def home(request):
     html='''Admin Page <a href="/admin">Click</a>'''
     return HttpResponse(html)
