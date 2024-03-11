from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User

# Create your views here.

def register(request):

    if request.method != "POST":
        return render(request, "register.html")
    data = request.POST
    customer_name = data.get('customer_name')
    customer_email = data.get('customer_email')
    customer_password = data.get('customer_password')
    customer_contact = data.get('customer_contact')
    customer_address = data.get("customer_address")
    customer_profile_image = request.FILES.get('customer_profile_image')


    CustomerRegistration.objects.create(
        customer_name = customer_name,
        customer_email = customer_email,
        customer_password = customer_password,
        customer_contact = customer_contact,
        customer_address = customer_address,
        customer_profile_image = customer_profile_image
    )  

    user = User.objects.create_user(customer_name, customer_email, customer_password)
    user.save()


    return redirect('login/')