from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from core.forms import JoinForm, LoginForm
from django.contrib.auth import login as auth_login

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request,'core/home.html')

def join(request):
    return render(request,'core/join.html')

def about(request):
    return render(request,'core/about.html')
def join(request):
    if (request.method == "POST"):
        join_form = JoinForm(request.POST)
        if (join_form.is_valid()):
            user = join_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("/")
        else:
            page_data = { "join_form": join_form }
            return render(request, 'core/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'core/join.html', page_data)
def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request,user)
                    return redirect("/")
                else:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'core/login.html', {"login_form": LoginForm})
    else:
        return render(request, 'core/login.html', {"login_form": LoginForm})
@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect("/")
