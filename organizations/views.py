from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def organization_list(request):
    # This view will list all organizations
    return HttpResponse("List of organizations")