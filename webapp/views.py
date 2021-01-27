from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from webapp.models import QPapers, notes, Texbook
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings




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



@login_required
def contact(request):

    if request.method == 'POST':
      message= request.POST['Message']
      email = request.POST['Emailing']
      send_mail(
      'Confirmation Email',
      message,
      settings.EMAIL_HOST_USER,
      [email],
      fail_silently=False,
     )
    return render(request, 'ContactUs.html')    

@login_required
def search(request):
  
   query = request.GET['select']
   if len(query)> 78:
     allpost =[]

   else:  
      allposttitle =Texbook.objects.filter(Title__icontains=query)
      allpostauth= Texbook.objects.filter(Author__icontains=query)
      allpostsub= Texbook.objects.filter(Subject__icontains=query)
      allpostint= allposttitle.union(allpostauth)
      allpost=allpostint.union(allpostsub)
    
      
     
      
      context = {
        'allpost':allpost
        }
   return render(request,'search.html',context)



  


def requestForm(request):
    return render(request, 'request1.html')

