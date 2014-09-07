from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def my_home_view(request):
    return HttpResponse("hiisadoasd")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date':now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})


def factorial(n):
    
    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)
    
        

def more_practice(request, n):
    n = int(n)
    return render(request, 'factorial.html', {'n': n, 'factorial': factorial(n)})
    
        