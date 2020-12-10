from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('Users-home')
        else:
            print(form.cleaned_data)
    else:    
        form = SignUpForm()
    return render(request, 'login_form.html', {'form':form})