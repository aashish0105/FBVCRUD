from django.shortcuts import render,redirect
from .forms import LaptopModelForm
from .models import Laptop
from django.contrib.auth.decorators import login_required
# Create your views here.


def add_laptop(request):
    form=LaptopModelForm()
    if request.method == 'POST':
        form = LaptopModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
    template_name = 'firstapp/addlaptop.html'
    context = {'form':form}
    return render(request,template_name,context)


def display_laptop(request):
    template_name = 'firstapp/displaylaptop.html'
    laptops = Laptop.objects.all()
    context = {'objs':laptops}
    return render(request,template_name,context)

def update_laptop(request,lid):
    obj = Laptop.objects.get(id=lid)
    form = LaptopModelForm(instance=obj)
    if request.method == 'POST':
        form = LaptopModelForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('display')
    template_name = 'firstapp/addlaptop.html'
    context = {'form':form}
    return render(request,template_name,context)

def delete_laptop(request,i):
    obj=Laptop.objects.get(id=i)
    obj.delete()
    return redirect('display')

