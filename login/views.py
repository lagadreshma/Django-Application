from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from register.models import CustomerRegistration

def loginCustomer(request):
    if request.method == 'POST':

        email = request.POST.get('customer_email')
        password = request.POST.get('customer_password')
        authenticated_user = authenticate(request, username=email, password=password)

        if authenticated_user is not None:
            return render(request, 'login.html', {'error_message': 'Invalid email or password.'})  

        login(request, authenticated_user)
        return redirect('/home/')
    

    return render(request, 'login.html')
