from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.

def adminLogin(request):

   if request.method != 'POST':
      return render(request, 'admin_login.html')
   email = request.POST.get('email')
   password = request.POST.get('password')

   if email != 'admin2024@gmail.com' or password != 'admin8899':
      return render(request, 'admin_login.html', {'error_message': 'Invalid email or password.'})
   # Authenticate and login the admin user
   user = authenticate(request, username=email, password=password)

   if user is None:
      return render(request, 'admin_login.html', {'error_message': 'Invalid credentials.'})
   login(request, user)
   return redirect('/admin_dashboard/')  # Redirect to admin dashboard


def adminDashboard(request):
   return render(request, "admin_dashboard.html")