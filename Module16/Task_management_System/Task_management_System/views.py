from django.shortcuts import render
from task.models import Task
def show_task(request):
    tasks = Task.objects.all()
    return render(request, 'show_task.html',{'tasks':tasks})