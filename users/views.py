from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def user_list(request):
    return JsonResponse({'message': 'List of users'})