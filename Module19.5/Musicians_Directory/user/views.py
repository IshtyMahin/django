from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import View
from . import forms

from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(View):
    def get(self,request):
        form = forms.RegisterForm()
        return render(request,'register.html',{'form':form,'type':'Signup'})
    
    def post(self,request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created for successfully')
            return redirect('signup')
        return render(request, 'register.html', {'form': form, 'type': 'Register'})
        

class UserLoginView(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request,'Logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,'Login information incorrect')
        return super().form_invalid(form)
    
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login' 
        return context
    

def user_logout(request):
    logout(request)
    messages.warning(request, 'Logout successfully completed')
    return redirect('login')
