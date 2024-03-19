from django.shortcuts import render,redirect
from .forms import InventoryForm
from .models import Inventory

# Create your views here.
def home(request):
  return render(request, 'home.html')

def inventory(request):
  if request.method == 'POST':
    form = InventoryForm(request.POST)
    try:
         if form.is_valid():
          form.save()
          return redirect('/show')
    except:
        pass
  else:
      form = InventoryForm()
  return render(request,'index.html',{'form':form})
  
def show(request):
  inventorys = Inventory.objects.all()
  total_price = sum(inventory.Iprice * inventory.Iquantity for inventory in inventorys)
  return render(request,'show.html',{ 'inventorys' : inventorys ,'total_price':total_price })

def edit(reuest,Iid):
  inventory=Inventory.objects.get(Iid=Iid)
  return render(reuest,'edit.html',{"inventory":inventory})

def update(request,Iid):
  inventory = Inventory.objects.get(Iid=Iid)
  form  = InventoryForm(request.POST,instance=inventory)
  if form.is_valid():
    form.save()
    return redirect('/show')
  return render(request,'edit.html',{"inventory":inventory})

def delete(request,Iid):
  inventory = Inventory.objects.get(Iid=Iid)
  inventory.delete()
  return redirect("/show")

