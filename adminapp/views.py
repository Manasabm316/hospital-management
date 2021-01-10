from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# from .forms import CreateUserForm
# from .models import * 
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.


def base(request):
    return render(request, 'adminapp/base.html')

def nav(request):
    return render(request, 'adminapp/navbar.html')

def footer(request):
    return render(request, 'adminapp/footer.html')

def adminsite(request):
    return render(request, 'adminapp/adminsite.html')


def doc_registration(request):
    # if request.session.get('doctor_name',None) and request.session.get('type',None)=='doctor':
    #     return redirect('doc_registration')
    if request.method=="POST":
        doctor_name=request.POST['doctor_name']
        email=request.POST['email']
        if Doctor.objects.filter(doctor_name=doctor_name) or Doctor.objects.filter(email=email):
           messages.warning(request,"Account already exist, please Login to continue")
        else:
            password=request.POST['password']
            specialization = request.POST['specialization']
            error=[]
            if(len(doctor_name)<3):
                error.append(1)
                messages.warning(request,"Doctor Name must be greater than 3 character.")
            if(len(password)<5):
                error.append(1)
                messages.warning(request,"Password Field must be greater than 5 character.")
            if(len(email)==0):
                error.append(1)
                messages.warning(request,"Email field can't be empty")
            if(len(specialization)==0):
                error.append(1)
                messages.warning(request,"Specializationd can't be empty")
            if(len(error)==0):
                password_hash = make_password(password)
                doctor=Doctor()
                doctor.save()
                messages.info(request,"Account Created Successfully, please Login to continue")
                redirect('doc_registration')
            else:
                redirect('doctorlogin')
        
    else:
        redirect('doc_registration')
    return render(request,'adminapp/doc_registration.html',{})