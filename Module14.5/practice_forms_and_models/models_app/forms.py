
from django import forms 
   

from .models import Model 
   
# create a ModelForm 
class ModelFrom(forms.ModelForm): 
    
    class Meta: 
        model = Model 
        fields = "__all__"