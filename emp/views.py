from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Emp
from .form import FeedbackForm 
# Create your views here.
def home(request):
    emps=Emp.objects.all()
    return render(request,"emp/home.html",{
        'emps':emps
    })
def addEmp(request):
    if request.method=="POST":
        #data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_departments=request.POST.get("emp_departments")

        #create model object and set data
        e=Emp()
        e.name=emp_name
        e.empId=emp_id
        e.empPhone=emp_phone
        e.address=emp_address
        e.department=emp_departments

        #objext save
        e.save()

        print("data is comming")
        return redirect("/emp/home/")

    return render(request,"emp/addEmp.html",{})

def delete(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    print(emp_id)
    return redirect("/emp/home/")

def update(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request,"emp/update_emp.html",{
        'emp':emp
    })

def do_update(request,emp_id):
    if request.method=='POST':
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_departments=request.POST.get("emp_departments")
        e=Emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.empId=emp_id_temp
        e.empPhone=emp_phone
        e.address=emp_address
        e.department=emp_departments
        e.save()
    return redirect("/emp/home/")
def Feedback(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
           form.save()
           print("data saved")
        else:
            return render(request,"emp/Feedback.html",{'form':form})
    else:
        form=FeedbackForm()
    return render(request,"emp/Feedback.html",{'form':form})