from django.shortcuts import render, redirect
from django.contrib import messages
import Users.forms
from .forms import SignUpForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def login(request):
    signupform = SignUpForm(request.POST)
    login_form = AuthenticationForm(data=request.POST)

    if request.method == 'POST':

            if signupform.is_valid():
                signupform.save()
                return redirect('Users-Homepage')

            elif login_form.is_valid():
                user_cred = request.POST['username']
                pwd = request.POST['password']
                user = authenticate(request, username=user_cred, password=pwd)
                if user is not None:
                    auth_login(request, user)
                    messages.success(request, f'You have logged into your account { user_cred } !!')
                    return redirect('Users-Homepage')
                else:
                    print('error')

            else:
                print(signupform)

    else:    
        signupform = SignUpForm()
    context = {
        'form': signupform,
        'login_form': login_form,
    }
    return render(request, 'login_form.html', context)