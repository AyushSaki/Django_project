from django.shortcuts import render,HttpResponse
from .models import Register,Student
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')   

def contact(request):
    
    if request.method=='POST':
        fname=request.POST.get('fname')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        password=request.POST.get('password')
        message=request.POST.get('message')
        student1=Student(fname=fname,contact=contact,email=email,password=password,message=message)
        student1.save()
        messages.success(request, "Your Message Has Been Sent Successfully.")

    return render(request,'contact.html') 

def training(request):
    return render(request,'training.html')

def gallery(request):
    return render(request,'gallery.html')

def register(request):
    
    if request.method=='POST':
        name=request.POST.get('name')
        lname=request.POST.get('lname')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        password=request.POST.get('password')
        hashed_password=make_password(password)
        message=request.POST.get('message')
        hobbies = request.POST.getlist('hobbies')
        gender = request.POST.get('gender')
        date = request.POST.get('date')  
        time = request.POST.get('time')     
        fileupload = request.FILES.get('fileupload')
        register1=Register(name=name,lname=lname,contact=contact,email=email,password=hashed_password,message=message,hobbies=hobbies,gender=gender,date=date,time=time,fileupload=fileupload)
        register1.save()
        messages.success(request, "form submitted successfully.")
        
    return render(request,'register.html')
    