from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

def redirectview(request):
    return redirect('/home/')  # Redirect root URL to /redirect/

def homeview(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())  # Redirect to an external URL
