from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from home.models import ServiceRequests
from register.models import CustomerRegistration

# Create your views here.
def homePage(request):
    return render(request, 'home.html')




def serviceRequests(request):

    if request.method != "POST":
        return render(request, "service_request.html")
    data = request.POST
    customer = request.user
    request_type = data.get('request_type')
    request_desc = data.get('details')
    request_attachment = request.FILES.get('attachment')

    ServiceRequests.objects.create(
        customer = customer,
        request_type = request_type,
        details = request_desc,
        attachment = request_attachment
    )

    return render(request, 'service_request.html')

def serviceStatus(request):
    service_requests = ServiceRequests.objects.filter(customer=request.user)
    return render(request, 'service_status.html', {'service_requests': service_requests})

def customerProfile(request):
    try:
        customer_registration = CustomerRegistration.objects.get(customer_name=request.user.username)
        return render(request, 'profile.html', {'customer_registation': customer_registration})
    except ObjectDoesNotExist:
        message = "Sorry, your profile does not exist."
        return render(request, 'profile.html', {'message': message})


def logoutUser(request):
    logout(request)
    return render(request, 'login.html')
