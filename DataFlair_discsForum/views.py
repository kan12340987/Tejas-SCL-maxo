from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
from django.contrib.auth.decorators import login_required

# Create your views here.
 
@login_required
def home(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'home.html',context)
 

@login_required
def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/forum')
    context ={'form':form}
    return render(request,'addInForum.html',context)
 

@login_required
def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/forum')
    context ={'form':form}
    return render(request,'addInDiscussion.html',context)
