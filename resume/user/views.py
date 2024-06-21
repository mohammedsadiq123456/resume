from django.shortcuts import render, reverse
from user.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http.response import HttpResponseRedirect

from user.functions import generate_form_errors


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            user = User.objects.create_user(
                username = instance.username,
                password = instance.password,
                email = instance.email,
            )

            user = authenticate(request, username=instance.username, password = instance.password)
            auth_login(request, user)

            return HttpResponseRedirect(reverse("user:index"))
        else:
            message = generate_form_errors(form)
            form = UserForm()
            context = {
                "title" : "Signup",
                "error" : True,
                "message" : message,
                "form" : form
            }
            return render(request, "signup.html", context = context)
    else:
        form = UserForm()
        context ={
            "title": "Signup",
            "form": form,
        }
        return render(request, "signup.html", context=context)
    

def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect("/")
            else:
                context = {
                    "error" : True,
                    "message" : "Invalid username or password",
                }
                return render(request, "login.html", context=context)
        else:
                context = {
                    "error" : True,
                    "message" : "Invalid username or password",
                }
                return render(request, "login.html", context=context)
    else:
        context = {
            "message" : "Invalid username or password",
        }
        return render(request, "login.html", context=context)

def index(request):
    return render(request, "ind.html")

