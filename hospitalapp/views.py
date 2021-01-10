from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from .models import Doctor, SlotRequest, Prescription, SlotAllocation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password,check_password
# Create your views here. 

def welcome(request):
    return render(request, 'hospitalapp/welcome.html')

def base(request):
    return render(request, 'hospitalapp/base.html')

def nav(request):
    return render(request, 'hospitalapp/nav.html')

def footer(request):
    return render(request, 'hospitalapp/footer.html')

def loginoptions(request):
    return render(request, 'hospitalapp/loginoptions.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            form.save()
            messages.success(request, 'Account created for ' +username)
            return redirect('patientlogin')
    else:
        form = CreateUserForm()
    return render(request, 'hospitalapp/register.html', {'form':form})

def patientlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return render(request, 'hospitalapp/patientlogin.html')
    
    context = {}
    return render(request, 'hospitalapp/patientlogin.html', context)

@login_required(login_url = 'patientlogin')
def dashboard(request):
    # list = Specialization.objects.all() 
    return render(request, 'hospitalapp/dashboard.html')#{'Specialization':list})

@login_required(login_url = 'patientlogin')
def slot_request(request):
    if request.method == 'POST':
        slotrequest = SlotRequest()
        slotrequest.patientname = request.POST.get('patientname')
        slotrequest.patientemail = request.POST.get('patientemail')
        slotrequest.patientsymptoms = request.POST.get('patientsymptoms')
        slotrequest.patientaddress = request.POST.get('patientaddress')
        slotrequest.doctorname = request.POST.get('doctorname')
        slotrequest.save()
        messages.success(request, 'Request Successfully Sent')
        return redirect('dashboard')

    return render(request, 'hospitalapp/slotbooking.html')

@login_required(login_url = 'patientlogin')
def patient_prescription(request):
    prescription = Prescription.objects.all()
    return render(request, 'hospitalapp/patient_prescription.html',{'Prescription':prescription})

def adminsite(request):
    return render(request, 'hospitalapp/admin.html')



def doc_registration(request):
    if request.session.get('doctor_name',None) and request.session.get('type',None)=='doctor':
        return redirect('doc_registration')
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
                doctor=Doctor(doctor_name=doctor_name,email=email,specialization=specialization,password=password_hash) 
                doctor.save()
                messages.info(request,"Account Created Successfully, please Login to continue")
                redirect('doctorlogin')
            else:
                redirect('doc_registration') 
        
    else:
        redirect('doc_registration')
    return render(request,'hospitalapp/doc_registration.html',{})

def doctorlogin(request):
    if request.session.get('doctor_name',None) and request.session.get('type',None)=='doctor':
        return redirect('doc_dashboard')
    if request.method=="POST": 
        doctor_name=request.POST['doctor_name'] 
        password=request.POST['password']
        if not len(doctor_name):
            messages.warning(request,"Doctor Name field is empty")
            redirect('doctorlogin')
        elif not len(password):
            messages.warning(request,"Password field is empty")
            redirect('doctorlogin')
        else:
            pass
        if Doctor.objects.filter(doctor_name=doctor_name):
            doctor1=Doctor.objects.filter(doctor_name=doctor_name)[0] 
            password_hash=doctor1.password
            res=check_password(password,password_hash)
            if res==1:
                request.session['doctor_name'] = doctor_name
                request.session['type'] = 'doctor'
                return render(request,'hospitalapp/doc_dashboard.html',{}) 
            else:
                messages.warning(request,"Username or password is incorrect")
                redirect('doctorlogin')
        else:
            messages.warning(request,"Account doesn't exist for the given Username")
            redirect('doctorlogin')
    else:
        redirect('doctorlogin')
    return render(request,'hospitalapp/doctorlogin.html',{}) 


#@login_required(login_url = 'doctorlogin') 
def doc_dashboard(request):
    return render(request, 'hospitalapp/doc_dashboard.html')

# @login_required(login_url = 'doctorlogin')
def doc_requests(request):
    slotrequest = SlotRequest.objects.all()
    return render(request, 'hospitalapp/doc_requests.html',{'SlotRequest':slotrequest})
# doctor is missing from hospitalapp

def doc_prescription(request):
    if request.method == 'POST': 
        prescription = Prescription() 
        prescription.patientname = request.POST.get('patientname')
        prescription.patientsymptom = request.POST.get('patientsymptom')
        prescription.doc_prescription = request.POST.get('prescription')
        prescription.save()
        messages.success(request, 'Prescription Successfully Sent')
        return redirect('doc_dashboard')

    return render(request, 'hospitalapp/doc_prescription.html')


def confirmslot(request):
    if request.method == 'POST': 
        slotallocation = SlotAllocation()
        slotallocation.slotpatient_name = request.POST.get('slotpatient_name')
        slotallocation.slotdoctor_name = request.POST.get('slotdoctor_name')
        slotallocation.slotspecialization = request.POST.get('slotspecialization')
        slotallocation.slotroom_id = request.POST.get('slotroom_id')
        slotallocation.slotdate = request.POST.get('slotdate')
        slotallocation.slotgender = request.POST.get('slotgender')
        slotallocation.save()
        return redirect('doc_dashboard')
       
    return render(request, 'hospitalapp/confirmslot.html')


@login_required(login_url = 'patientlogin')
def logoutUser(request):
    logout(request)
    return redirect('patientlogin')    
