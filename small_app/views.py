from django.shortcuts import render
from .forms import Emp_forms
from .models import Emp

def home(request):
    fo=Emp_forms()
    qs=Emp.objects.all()
    return render(request, "home.html", {"home": fo},{"data":qs})


def save(request):
    name=request.POST.get("name")
    age=request.POST.get("age")
    dept=request.POST.get("dept")
    salry=request.POST.get("salary")
    Emp(name=name,age=age,dept=dept,salary=salry).save()
    res=Emp.objects.all()
    return render(request,"reg.html",{"result":res})








