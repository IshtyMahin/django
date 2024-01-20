from django.shortcuts import render
from datetime import datetime

def blogs(request):
    blog = {
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Inventore quisquam accusantium mollitia repudiandae laudantium sint, maiores repellendus nulla sit vel nostrum facilis voluptatem, eveniet animi?',
        'pub_date':datetime.strptime("2023-01-12T10:30:00.000123", "%Y-%m-%dT%H:%M:%S.%f").date(),
        'author': 'John Doe',
        'tags': ['python', 'django'],
    }
    return render(request, 'index.html', context={'blog': blog})
