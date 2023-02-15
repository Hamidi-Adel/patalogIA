from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import signupForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import User

def accounts(request):
    form = signupForm(request.POST or None)
    email_exist = User.objects.filter(email=request.POST.get('email')).exists()
    username_exist = User.objects.filter(username=request.POST.get('username')).exists()
    if request.method == 'POST' and form.is_valid():
        form.save()
    else:
        if request.POST.get('confirm_password') != request.POST.get('password'):
            messages.error(request, "Password Doesn't match")
        elif email_exist:
            messages.error(request, "Email already exists!")
        elif username_exist:
            messages.error(request, "This username is already in use")    
    context = {'signup':form}
    return render(request, 'accounts/accounts.html', context)

def loginUser(request):
    if request.method == 'POST':
        userEmail = request.POST.get('email')
        rawPassword = request.POST.get('password')
        user = authenticate(email=userEmail, password=rawPassword)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                print('superuser')
            elif not user.is_superuser:    
                generalInfo = User.objects.get(email = userEmail)
                if str(generalInfo.usertype) == "Student":
                    login(request, user)
                    return redirect("questions:quiz")
                elif str(generalInfo.usertype) == "Guest":
                    login(request, user)
                    return redirect("questions:quiz")
                elif str(generalInfo.usertype) == "Teacher":
                    login(request, user)
                    return redirect("questions:dashboard")
                    
        else:
            messages.error(request, "Username or Password is Wrong")
            return redirect('registration:loginPage')
    return render(request, 'accounts/login.html')

def logoutUser(request):
    logout(request)
    return render(request, 'accounts/login.html')
