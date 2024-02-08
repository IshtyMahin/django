from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Car,Brand
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import DetailView

def admin_check(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(admin_check)
def add_car(request):
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST)
        if car_form.is_valid():
            car_form.save()
            return redirect('home')
        
    else:
        car_form = forms.CarForm()
        
    return render(request,'add_car.html',{'form': car_form})
@user_passes_test(admin_check)
def add_brand(request):
    if request.method == 'POST':
        brand_form = forms.BrandForm(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            return redirect('home')
        
    else:
        brand_form = forms.BrandForm()
        
    return render(request,'add_brand.html',{'form': brand_form})



@user_passes_test(admin_check)
def edit_car(request,id):
    car = Car.objects.get(id=id)
    car_form = forms.CarForm(instance=car)
    
    if request.method == 'POST':
        car_form = forms.CarForm(request.POST,instance=car)
        if car_form.is_valid():
            car_form.save()
            return redirect('home')
        
    return render(request,'edit_car.html',{'form': car_form})



@user_passes_test(admin_check)
def delete_car(request,id):
     car = Car.objects.get(pk=id)
     car.delete()
     return redirect('home')
 

class DetailPostView(DetailView):
    model = Car 
    template_name = 'car_details.html'
    
    def post(self, request, *args, **kwargs):
        comments_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comments_form.is_valid():
                new_comments= comments_form.save(commit=False)
                new_comments.post = post 
                new_comments.save()
        return self.get(request,*args,**kwargs)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object 
        comments = car.comments.all()
        
        comments_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comments_form'] = comments_form
        return context