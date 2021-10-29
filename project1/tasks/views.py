from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from tasks.forms import TaskEntryForm
from django.contrib.auth.models import User
from tasks.forms import TaskEntryForm
from tasks.models import TaskCategory, Task
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def tasks(request):
    if(request.method=="GET" and "delete" in request.GET):
        id=request.GET["delete"]
        Task.objects.filter(id=id).delete()
        return redirect("/tasks")
    else:
        table_data=Task.objects.filter(user=request.user)
        context={"table_data":table_data}
        return render(request, 'tasks/tasks.html', context)
    if(request.method=="GET"and "toggle" in request.GET):
        return redirect("/")
        toggle_is_completed=Task(request.GET)
        if(toggle_is_completed.is_valid()):
            if(Task.objects.filter(user=request.user, is_completed='False')):
                return redirect("/")

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
    elif(request.method=="POST" and "edit" in request.POST):
        form=TaskEntryForm(request.POST)
        if(form.is_valid()):
            task=form.save(commit=False)
            task.user=request.user
            task.id=id
            task.save()
            return redirect("/tasks/")
        else:
            context={"form_data":form}
            return render(request, 'tasks/add.html', context)
    else:
        return redirect("/tasks/")
