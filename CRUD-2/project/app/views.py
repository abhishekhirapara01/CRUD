from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm

# Create your views here.
def home(request):
  return render(request,'home.html')

def stu(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    try:
         if form.is_valid():
          form.save()
          return redirect('/show')
    except:
        pass
  else:
      form = StudentForm()
  return render(request,'index.html',{'form':form})      

def show(request):
   students = Student.objects.all()
   return render (request,'show.html',{'students':students})

def edit(request,Sroll_num):
   student = Student.objects.get(Sroll_num=Sroll_num)
   return render(request,'edit.html',{'student':student})

def update(request,Sroll_num):
   student = Student.objects.get(Sroll_num=Sroll_num)
   if request.method=='POST':
     form =StudentForm(request.POST,instance=student)
     if form.is_valid():
       form.save()
       return redirect('/show')
   else:
     form = StudentForm(instance=student)
   return render(request,"update.html",{"form":form})

def delete(request,Sroll_num):
   student = Student.objects.get(Sroll_num=Sroll_num)
   student.delete()
   return redirect("/show")