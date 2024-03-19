from django.shortcuts import render,redirect
from .forms import EventForm
from .models import Event

# Create your views here.
def home(request):
  return render(request, 'home.html')

def event(request):
  if request.method == 'POST':
    form = EventForm(request.POST)
    try:
         if form.is_valid():
          form.save()
          return redirect('/show')
    except:
        pass
  else:
      form = EventForm()
  return render(request,'index.html',{'form':form})
  
def show(request):
  events = Event.objects.all()
  return render(request,'show.html',{ 'events' : events })

def edit(reuest,Eid):
  event=Event.objects.get(Eid=Eid)
  return render(reuest,'edit.html',{"event":event})

def update(request,Eid):
  event = Event.objects.get(Eid=Eid)
  form  = EventForm(request.POST,instance=event)
  if form.is_valid():
    form.save()
    return redirect('/show')
  return render(request,'edit.html',{"event":event})

def delete(request,Eid):
  event = Event.objects.get(Eid=Eid)
  event.delete()
  return redirect("/show")

