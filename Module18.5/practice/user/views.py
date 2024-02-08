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
    

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
    
        return render(request, 'profile.html')
    

class EditProfileView(LoginRequiredMixin,View):
    
    def get(self, request):
        form = forms.ChangeUserForm(instance=request.user)
        return render(request, 'update_profile.html', {'form': form})

    def post(self, request):
        form = forms.ChangeUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        
        return render(request, 'update_profile.html', {'form': form})
        

class PasswordChangeView(LoginRequiredMixin,View):
    
    def get(self,request):
        form = PasswordChangeForm(user=request.user)
        return render(request,'pass_change.html',{'form': form})
    

    def post(self,request):
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated successfully')
            return redirect('profile')
        return render(request, 'pass_change.html', {'form': form})  
    
class Without_Old_pass_PasswordChangeView(LoginRequiredMixin,View):
    
    def get(self,request):
        form = SetPasswordForm(user=request.user)
        return render(request,'pass_change.html',{'form': form})
    

    def post(self,request):
        form = SetPasswordForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated successfully')
            return redirect('profile')
        return render(request, 'pass_change.html', {'form': form})  
    

def user_logout(request):
    logout(request)
    messages.warning(request, 'Logout successfully completed')
    return redirect('login')
