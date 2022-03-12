from django.shortcuts import render
from django.http import HttpResponseRedirect
from testapp.models import Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from testapp.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@method_decorator(login_required, name='dispatch')
class CompanyListView(ListView):
    login_required = True
    model=Company
   
    
    
@method_decorator(login_required, name='dispatch')
class CompanyDetailView(DetailView):
    login_required = True
    model=Company
    

@method_decorator(login_required, name='dispatch')
class CompanyCreateView(CreateView):
    model=Company
    fields = ('name','location','ceo')

@method_decorator(login_required, name='dispatch')
class CompanyUpdateView(UpdateView):
    model=Company
    fields=('name','ceo')

@method_decorator(login_required, name='dispatch')
class CompanyDeleteView(DeleteView):
   model=Company
   success_url = reverse_lazy('companies')



def base(request):
    return render(request,'testApp/base.html')


def logout_view(request):
    return render(request,'testApp/logout.html')

def sign_up_view(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save() 
            return HttpResponseRedirect('/accounts/login')
    return render(request,'testApp/signup.html',{'form':form})



