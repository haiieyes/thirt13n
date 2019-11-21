from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def index(request):
    return render(request, 'index.template.html')
    
def album(request):
    return render(request, 'accounts/album.template.html')
    
def music(request):
    return render(request, 'accounts/music.template.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return render(request, 'accounts/reindex.template.html')
    
def login(request):
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            messages.success(request, "You have successfully logged in")
            if user:
                auth.login(user=user, request=request)
                return render(request, 'accounts/reindex.template.html')
            else:
                login_form.add_error(None, "Invalid username or password")
                return render(request, 'accounts/login.template.html', {
                  'form':login_form
                })

    else:
        login_form = UserLoginForm()
        return render(request, 'accounts/login.template.html', {
            'form':login_form
        })

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully signed up!")
            else:
                messages.error(request, "Whoops, we are unable to register your account at this time.")
            return render(request, 'accounts/reindex.template.html')
        else:
            return render(request, 'accounts/register.template.html', {
                'form':form
            })
    else:
        form = UserRegistrationForm()
        return render(request, 'accounts/register.template.html', {
            'form':form
        })

def shop(request):
    return render(request, 'shop.template.html')