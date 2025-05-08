from django.http import JsonResponse

# Create your views here.
def user_list(request):
    return JsonResponse({'message': 'List of users'})

