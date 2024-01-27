from django.shortcuts import render
from .forms import PracticeForm
# Create your views here.


def home_view(request):
    context = {}
    context['form'] = PracticeForm()
    return render(request,'forms.html',context)
