from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    print User
    return render(request, 'login_and_registration_app/index.html')
# Create your views here.

def register(request):
    res = User.objects.register(request.POST)

    if res["added"]:
        messages.success(request, "Success! Welcome {}! Successfully registered!".format(res["new_user"].first_name))
        return render(request, 'login_and_registration_app/success.html')
    else:
        for error in res["errors"]:
            messages.error(request, error)
            return redirect('/')

def login(request):
    res = User.objects.login(request.POST)

    if res:
        messages.success(request, "Success! Welcome {}! Successfully logged in!".format(res[1].first_name))
        return render(request, 'login_and_registration_app/success.html')
    else:
        messages.success(request, "Invalid email or password")
        return redirect('/')
