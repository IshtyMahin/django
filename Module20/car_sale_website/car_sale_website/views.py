from django.shortcuts import render
from car.models import Car,Brand 
# Create your views here.

def home(request,brand_slug=None):
    data = Car.objects.all()
    
    if brand_slug is not None :
        brand = Brand.objects.get(slug = brand_slug)
        print(brand)
        data = Car.objects.filter(brand_name = brand)
        
    brands = Brand.objects.all()
    return render(request, 'home.html', {'data': data, 'brands':brands})