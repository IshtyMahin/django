from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views import View
from . import forms
from car.models import Car ,Purchase
from django.contrib.auth.decorators import login_required
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
            return redirect('login')
        return render(request, 'register.html', {'form': form, 'type': 'Register'})
        

class UserLoginView(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
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
        purchased_cars = Purchase.objects.filter(user=request.user)
        print(purchased_cars.count)
        return render(request, 'profile.html', {'data': purchased_cars})
    

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
    

def user_logout(request):
    logout(request)
    return redirect('login')


def buy_car(request,id):
    if request.method == 'GET':
       car = Car.objects.get(id=id)
       purchase = Purchase(user=request.user,car=car)
       purchase.save()
       
       if car.quantity > 0:
           car.quantity -=1
           car.save()
        
       return redirect('profile')
   
def delete_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    
    if request.method == 'POST':
        purchase.car.quantity +=1
        print(purchase.car.quantity)
        purchase.car.save()
        
        purchase.delete()
        return redirect('profile')