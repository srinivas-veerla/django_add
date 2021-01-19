from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import History
# Create your views here.
def home(request):
    return render(request,'Add.html')

def add(request):
    if request.method=='POST':
        if request.POST['num1'] and request.POST['num2']:
            n1=int(request.POST['num1'])
            n2=int(request.POST['num2'])
            res=n1+n2
            his=History()
            his.num1=n1
            his.num2=n2
            his.res=res
            his.save()
            return render(request,'result.html',{'result':res})
        else:
            return HttpResponseRedirect('/') 

def his(request):
    history=History.objects.all()
    
    if request.method=='POST':
        if request.POST['response']=='del':
            history=History.objects.all().delete()
            return HttpResponseRedirect('history') 

        elif request.POST['response']=='add':
            return HttpResponseRedirect('/')
    context={'history':history}
    return render(request,'history.html',context)