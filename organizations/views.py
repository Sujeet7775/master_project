from django.http import HttpResponse

# Create your views here.
def organization_list(request):
    # This view will list all organizations
    return HttpResponse("List of organizations")


