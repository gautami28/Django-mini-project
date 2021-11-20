from django.shortcuts import render
from django.contrib import messages
from . forms import *
from django.shortcuts import redirect
from django.views import View


# Create your views here.
def success(request):
    return render(request,'app/succ.html')
    
class register(View):
    def get(self,request):
        form = studform()
        context = {
            'form':form
        }
        return render(request, 'app/home.html',context)
    
    def post(self,request):
        form = studform(request.POST)
        if form.is_valid():
            messages.success(request,"User addes succesfully!!")
            form.save()
        context = {
            'form':form
        }
        return render(request,'app/home.html',context)
   