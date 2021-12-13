from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from app1.models import Board
from app1.forms import ChessForm
from app1.forms import JoinForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from app1.forms import ChessForm, JoinForm, LoginForm
# Create your views here.
def newGame(request):
    page_data={
        "rows":[
            {"a8":"&#9820", "b8":"&#9822;", "c8":"&#9821;" , "d8":"&#9819;", "e8":"&#9818;", "f8":"&#9821;", "g8":"&#9822;", "h8": "&#9820"},
            {"a7":"&#9823;", "b7":"&#9823;", "c7":"&#9823;" , "d7":"&#9823;", "e7":"&#9823;", "f7":"&#9823;", "g7":"&#9823;", "h7": "&#9823;"},
            {"a6":"&nbsp;", "b6":"&nbsp;", "c6":"&nbsp;" , "d6":"&nbsp;", "e6":"&nbsp;", "f6":"&nbsp;", "g6":"&nbsp;", "h6": "&nbsp;"},
            {"a5":"&nbsp;", "b5":"&nbsp;", "c5":"&nbsp;" , "d5":"&nbsp;", "e5":"&nbsp;", "f5":"&nbsp;", "g5":"&nbsp;", "h5": "&nbsp;"},
            {"a4":"&nbsp;", "b4":"&nbsp;", "c4":"&nbsp;" , "d4":"&nbsp;", "e4":"&nbsp;", "f4":"&nbsp;", "g4":"&nbsp;", "h4": "&nbsp;"},
            {"a3":"&nbsp;", "b3":"&nbsp;", "c3":"&nbsp;" , "d3":"&nbsp;", "e3":"&nbsp;", "f3":"&nbsp;", "g3":"&nbsp;", "h3": "&nbsp;"},
            {"a2":"&#9817;", "b2":"&#9817;", "c2":"&#9817;" , "d2":"&#9817;", "e2":"&#9817;", "f2":"&#9817;", "g2":"&#9817;", "h2": "&#9817;"},
            {"a1":"&#9814;", "b1":"&#9816;", "c1":"&#9815;" , "d1":"&#9813;", "e1":"&#9812;", "f1":"&#9815;", "g1":"&#9816;", "h1": "&#9814;"},
        ]
    }
    Board.objects.filter(user=request.user).delete()

    for row in page_data.get("rows"):
        for name,value in row.items():
            Board(user=request.user, location=name, value=value).save()
@login_required(login_url='/login/')
def home(request):
    if((Board.objects.filter(user=request.user).count() == 0)or (request.method=='GET' and 'reset' in request.GET)):
        newGame(request)

    page_data = {"rows": [], "chess_form":ChessForm}

    if(request.method == 'POST'):
        chess_form = ChessForm(request.POST)
        if(chess_form.is_valid()):
            dst = chess_form.cleaned_data["dst"]
            src = chess_form.cleaned_data["src"]
            rec = Board.objects.get(user=request.user, location=src)
            Board.objects.filter(user=request.user, location=dst).delete()
            Board.objects.filter(user=request.user, location=src).delete()
            Board(user=request.user, location=dst, value=rec.value).save()
            Board(user=request.user, location=src, value="&nbsp;").save()
        else:
            page_data["chess_form"]=chess_form

    for row in range(8,0,-1):
        row_data={}
        for col in range(97,105):
            id = "{}{}".format(chr(col),row)
            try:
                record = Board.objects.get(user=request.user, location=id)
                row_data[id]=record.value
            except Board.DoesNotExist:
                row_data[id]=chr(97)
        page_data.get("rows").append(row_data)

    return render(request,'app1/home.html', page_data)
def history(request):
    return render(request,'app1/history.html')
def summary(request):
    return render(request,'app1/summary.html')
def about(request):
    return render(request,'app1/about.html')
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
            return render(request, 'app1/join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = { "join_form": join_form }
        return render(request, 'app1/join.html', page_data)
def user_login(request):
    if (request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect("/")
                else:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return render(request, 'app1/login.html', {"login_form": LoginForm})
    else:
        return render(request, 'app1/login.html', {"login_form": LoginForm})
@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect("/")
