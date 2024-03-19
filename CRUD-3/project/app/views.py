
from django.shortcuts import render,redirect
from .forms import BookForm
from .models import Book

# Create your views here.
def home(request):
  return render(request, 'home.html')

def book(request):
  if request.method == 'POST':
    form = BookForm(request.POST)
    try:
         if form.is_valid():
          form.save()
          return redirect('/show')
    except:
        pass
  else:
      form = BookForm()
  return render(request,'index.html',{'form':form})
  
def show(request):
  books = Book.objects.all()
  return render(request,'show.html',{ 'books' : books })

def edit(reuest,Bid):
  book=Book.objects.get(Bid=Bid)
  return render(reuest,'edit.html',{"book":book})

def update(request,Bid):
  book = Book.objects.get(Bid=Bid)
  form  = BookForm(request.POST,instance=book)
  if form.is_valid():
    form.save()
    return redirect('/show')
  return render(request,'edit.html',{"book":book})

def delete(request,Bid):
  employee = Book.objects.get(Bid=Bid)
  employee.delete()
  return redirect("/show")

