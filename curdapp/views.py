from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from curdapp.models import *
from curdapp.forms import *


def home(request):
    return HttpResponse("Hello")

def read(request):
    student=Student.objects.all()
    return render(request,'read.html',{'student':student})

def create(request):
    if request.method=='POST':
        form=Studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
    form=Studentform()
    return render(request,'create.html',{'form':form})

def update(request,id):
    student=get_object_or_404(Student,id=id)
    if request.method=="POST":
        form=Studentform(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('read')
    form=Studentform(instance=student)
    return render(request,'update.html',{'form':form})

def deletestudent(request,id):
     student=get_object_or_404(Student,id=id)
     if request.method=="POST":
         student.delete()
         return redirect('read')
     return render(request,'delete.html')



