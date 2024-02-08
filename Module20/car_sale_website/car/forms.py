from django import forms 

from .models import Car,Brand,Comment
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
        
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ["name"]
        
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']