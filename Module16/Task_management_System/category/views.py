from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('show_task')
        
    else:
        category_form = forms.CategoryForm()
    return render(request,'add_task.html',{'form':category_form})