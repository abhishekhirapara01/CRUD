from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student
# Create your views here.

def home(request):
    return render(request,"home.html")

def stu(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('/show')
        except:
            pass
    else:
        form = StudentForm()
        return render(request, 'index.html',{'form':form})
    
def show(request):
    searchTerm = request.GET.get('searchStudent')
    if searchTerm:
        students = Student.objects.filter(name__icontains=searchTerm)
    else:    
        students = Student.objects.all().order_by('sid')
    return render(request, 'show.html',{'students':students,'searchTerm':searchTerm})

def edit(request, sid):
    student = Student.objects.get(sid=sid)
    return render(request, 'edit.html',{'student':student})

def update(request, sid):
    student = Student.objects.get(sid=sid)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html',{'student':student})
    
def delete(request, sid):
    student = Student.objects.get(sid=sid)
    student.delete()
    return redirect('/show')