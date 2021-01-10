from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from webapp.models import QPapers, notes, Texbook
from django.contrib.auth.models import User
from django.template import loader
from django.template.loader import get_template 
from . import models

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'About_us.html')

@login_required
def notebook(request):
    context = {
        'notes': notes.objects.all()
    }
    return render(request, 'NotebookSecondary.html',context)

@login_required
def questionpapers(request):
    context = {
        'qpapers': QPapers.objects.all()
    }
    return render(request, 'QuestionPaperSecondary.html', context)

@login_required
def textbook(request):
    context = {
        'textbook': Texbook.objects.all()
    }
    return render(request, 'TextbookSecondary.html',context)

@login_required
def landingpage(request):
    return render(request, 'Secondarylogin.html')


def search(request):
  if request.method == 'GET':
     search = request.GET.get('search')
     post= Texbook.objects.all().filter(Title=search)
     return render(request,'message.html',{'post':post})



