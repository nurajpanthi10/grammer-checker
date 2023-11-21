# appname/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from users.models import User

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Replace 'dashboard' with your desired URL
        else:
            error_message = "Invalid username or password."
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

def registration_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        mobile_number = request.POST['mobile_number']
        password2 = request.POST['password2']
        if password != password2:
            error_message = "Password and confirm password does not matched."
        else:
            new_user = User.objects.create(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                mobile_number=mobile_number
                )
            new_user.set_password(password)
            new_user.save()
            return redirect('login')  # Replace 'dashboard' with your desired URL
    else:
        error_message = None
    return render(request, 'registration.html', {'error_message': error_message})