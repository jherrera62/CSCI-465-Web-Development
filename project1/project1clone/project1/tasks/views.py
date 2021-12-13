from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from tasks.forms import TaskEntryForm
from django.contrib.auth.models import User
from tasks.forms import TaskEntryForm
from tasks.models import TaskCategory, Task
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from core.models import UserProfile
from core.forms import UserProfileMF
import json

# Create your views here.
@login_required(login_url='/login/')
def tasks(request):
##    checks=UserProfile.objects.filter(user=request.user)
    user=User.objects.get(id=request.user.id)
    checks=UserProfile(user=user, tasks_view_hide_completed=False)
    check=checks.tasks_view_hide_completed
    if(not TaskCategory.objects.all()):
        TaskCategory.objects.create(category="Home")
        TaskCategory.objects.create(category="School")
        TaskCategory.objects.create(category="Work")
        TaskCategory.objects.create(category="Self Improvement")

    if(request.method=="GET" and "delete" in request.GET):
        id=request.GET["delete"]
        Task.objects.filter(id=id).delete()
        return redirect("/tasks")
    elif(request.method=="GET"and "toggle" in request.GET):
        id=request.GET["toggle"]
        task=Task.objects.get(id=id)
        task.is_completed=not task.is_completed
        task.save()
#    try:
#        checks=UserProfile.objects.get(user=request.user, tasks_view_hide_completed=True)
#        check=checks.tasks_view_hide_completed
#    except UserProfile.DoesNotExist:
#        check=False
    if(request.method=="POST"):
        checks.change()
#        checks.tasks_view_hide_completed=not checks.tasks_view_hide_completed
        checks.save()
        check=checks.tasks_view_hide_completed
        print(checks.tasks_view_hide_completed)
#        id=request.POST
#        checks=UserProfile.objects.get(id=id)
#        checks.change()
#        check=checks.tasks_view_hide_completed
#        if(check):
#            print("TRUE")
#            check=False
#        else:
#            print("FALSE")
#            check=True
#        checks.save()
#        form=UserProfileMF(request.POST)
#        if(form.is_valid()):
#            user=User.objects.get(id=request.user.id)
#            check=form.cleaned_data["tasks_view_hide_completed"]
#            UserProfile(user=user, tasks_view_hide_completed=not check).save()
    table_data=Task.objects.filter(user=request.user)
    context={"table_data":table_data, "check":check}
#    return render(request, 'tasks/tasks.html', context)
    return render(request, 'tasks/tasks.html', context)
def add(request):
    if (request.method=="POST"):
        if("add" in request.POST):
            add_form=TaskEntryForm(request.POST)
            if(add_form.is_valid()):
                description=add_form.cleaned_data["description"]
                category=add_form.cleaned_data["category"]
                user=User.objects.get(id=request.user.id)
                TaskCategory(category=category).save()
                categories=TaskCategory(category=category)
                categories.save()
                Task(user=user, description=description, category=categories ,is_completed='False').save()
                return redirect("/tasks/")
            else:
                context = {"form_data":add_form}
                return render(request, 'tasks/add.html', context)
        else:
            return redirect("/tasks/")
    else:
        context = {
            "form_data": TaskEntryForm()
        }
        return render(request, 'tasks/add.html', context)
def edit(request, id):
    if(request.method=="GET"):
        task=Task.objects.get(id=id)
        form=TaskEntryForm(instance=task)
        context={"form_data": form}
        return render(request, 'tasks/edit.html', context)
    elif(request.method=="POST"):
        form=TaskEntryForm(request.POST)
        if(form.is_valid()):
            print("work")
            task=form.save(commit=False)
            task.user=request.user
            task.id=id
            task.is_completed=False
            task.save()
            return redirect("/tasks/")
        else:
            context={"form_data":form}
            return render(request, 'tasks/add.html', context)
    else:
        return redirect("/tasks/")
