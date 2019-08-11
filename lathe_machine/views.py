from django.shortcuts import render
from lathe_machine.models import Customer


# Create your views here.
def home(request):
    return render (request,'home.html',{})


def customer(request):
    obj=Customer.objects.all()
    return render(request,'customer.html',{'obj':obj})