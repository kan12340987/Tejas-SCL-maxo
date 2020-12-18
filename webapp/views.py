from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'About_us.html')

def notebook(request):
    return render(request, 'Notebook.html')

@login_required
def landingpage(request):
    return render(request, 'Secondarylogin.html')

