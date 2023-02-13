from django.shortcuts import render,redirect
from .models import *
from .forms import EmployeForm



def home(request):
    load = HomeReaload.objects.all()
    service  = servicesDescript.objects.all()
    about = About.objects.all()
    why_choseMe = Why_Choose_Us.objects.all()
    team = Tema.objects.all()
    context = {
        'load':load,'service':service,
        'about':about,'why_choseMe':why_choseMe,
        'team':team,
    }
    
    
    return render(request,'computerService/index.html',context)




def project_view(request):
    proje = Project.objects.all()
    context = {
          'proje':proje
    }
    
    
    return render(request,'computerService/project.html',context)



def Abouts(request):
    service  = servicesDescript.objects.all()
    about = About.objects.all()
    team = Tema.objects.all()
    context = {
        'service':service,
        'about':about,
        'team':team,
    }
    return render(request,'computerService/about.html',context)




def service(request):
    return render(request,'computerService/servuce.html',{})



def sucsess (request):
    return render(request,'computerService/suc.html',{})
    



def Employe(request):
    form = EmployeForm()
    if request.method == 'POST':
        form = EmployeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(sucsess)
        
    return render(request,'computerService/emp.html',{'form':form})
