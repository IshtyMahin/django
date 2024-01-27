from django.shortcuts import render
from .forms import ModelFrom
# Create your views here.


def models_view(request):
    context = {}
    context['form'] = ModelFrom()
    return render(request,'models.html',context)
