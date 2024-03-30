from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms 

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', }))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ChangeUserData(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
        