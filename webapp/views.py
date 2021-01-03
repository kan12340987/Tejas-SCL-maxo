from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from webapp.models import QPapers, notes, Texbook
from django.contrib.auth.models import User

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
    return render(request, 'TextbookSecondary.html')

@login_required
def landingpage(request):
    return render(request, 'Secondarylogin.html')

