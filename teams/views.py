from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def team_list(request):
    return HttpResponse({'message': 'List of teams'})