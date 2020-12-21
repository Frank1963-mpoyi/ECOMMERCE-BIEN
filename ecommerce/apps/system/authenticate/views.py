from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
#import Django buidin Userregistration form 
from django.contrib.auth.forms import UserCreationForm
#for logout to avoid anonymous user
from django.contrib.auth.decorators import login_required
from .forms import  CreateUserForm
from django.contrib import messages







def registerPage(request):
    template_name           = "authenticate/register.html"
    #we do manually coded not very nice way
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form                = CreateUserForm()
        if request.method   == "POST":
            form            = CreateUserForm(request.POST or None)
            if form.is_valid():
                form.save()
                #just to get a user name to display in the message
                user        = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ user)
                return redirect('login')
        context             = {
            'form': form
        }
        return render (request, "authenticate/register.html", context)




def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method   == "POST":
            # let grap username and password from userin frontend
            username        = request.POST.get('username')
            password        = request.POST.get('password')
            
            #after getting username and password let authenticate
            user            = authenticate(request, username=username, password=password)
            #before authenticate let check if user is there
            if user is not None:
                login(request, user)#we will login this user
                return redirect('home')
            else:
                messages.info(request, "Username OR Passowrd is incorrect")
        
        template_name       = "authenticate/login.html"
        context             = {
            
        }
        return render (request,template_name, context)


def logoutUser(request):
    logout(request)
    return redirect ("login")


