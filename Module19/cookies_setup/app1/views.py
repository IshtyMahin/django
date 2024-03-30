from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
# Create your views here.
def home(request):
    response = render(request,'home.html')
    # response.set_cookie('name','rahim',max_age=60*3)  
    response.set_cookie('name','rahim',expires=datetime.utcnow()+timedelta(days=7))  
    
    return response


def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request,'get_cookie.html',{'name':name})

def delete_cookie(request):
    response = render(request,'del.html')
    response.delete_cookie('name')
    return response


def set_session(request):
    data = {
        'name':'rahim',
        'age':23,
        'language':'Bangla'
    }
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date())
    request.session.update(data)
    return render(request,'home.html')


def get_session(request):
    if "name" in request.session:
        data = request.session
        request.session.modified = True
        return render(request,'get_session.html',{'data':data})
    
    else:
        return HttpResponse("Your session is expired. Please try again")

def del_session(request):
    request.session.flush()
    return render(request,'del_session.html')