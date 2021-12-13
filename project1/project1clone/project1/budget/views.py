from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from budget.forms import BudgetEntryForm
from django.contrib.auth.models import User
from budget.forms import BudgetEntryForm
from budget.models import BudgetCategory, Budget
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def budget(request):
    if(not BudgetCategory.objects.all()):
        BudgetCategory.objects.create(category="Food")
        BudgetCategory.objects.create(category="Clothing")
        BudgetCategory.objects.create(category="Housing")
        BudgetCategory.objects.create(category="Education")
        BudgetCategory.objects.create(category="Entertainment")
        BudgetCategory.objects.create(category="Other")
    if(request.method=="GET" and "delete" in request.GET):
        id=request.GET["delete"]
        Budget.objects.filter(id=id).delete()
        return redirect("/budget")
    else:
        table_data=Budget.objects.filter(user=request.user)
        total=0
        for each in table_data:
            total=(total)+(each.projected - each.actual)
        return render(request, 'budget/budget.html', {"table_data":table_data, "total":total})


def add(request):
    if (request.method=="POST"):
        if("add" in request.POST):
            add_form=BudgetEntryForm(request.POST)
            if(add_form.is_valid()):
                description=add_form.cleaned_data["description"]
                category=add_form.cleaned_data["category"]
                projected=add_form.cleaned_data["projected"]
                actual=add_form.cleaned_data["actual"]
                user=User.objects.get(id=request.user.id)
                BudgetCategory(category=category).save()
                categories=BudgetCategory(category=category)
                categories.save()
                Budget(user=user, description=description, category=categories , projected=projected, actual=actual).save()
                return redirect("/budget/")
            else:
                context = {"form_data":add_form}
                return render(request, 'budget/add.html', context)
        else:
            return redirect("/budget/")
    else:
        context = {
            "form_data": BudgetEntryForm()
        }
        return render(request, 'budget/add.html', context)
def edit(request, id):
    if(request.method=="GET"):
        bud=Budget.objects.get(id=id)
        form=BudgetEntryForm(instance=bud)
        context={"form_data": form}
        return render(request, 'budget/edit.html', context)
    elif(request.method=="POST"):
        form=BudgetEntryForm(request.POST)
        if(form.is_valid()):
            print("workeee")
            bud=form.save(commit=False)
            bud.user=request.user
            bud.id=id
            bud.save()
            return redirect("/budget/")
        else:
            context={"form_data":form}
            return render(request, 'budget/add.html', context)
    else:
        return redirect("/budget/")
