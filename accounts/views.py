from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import signupForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import User

def accounts(request):
    form = signupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
    else:
        if request.POST.get('confirm_password') != request.POST.get('password'):
            messages.error(request, "Password Doesn't match")
        else:
            form.errors
    context = {'signup':form}
    return render(request, 'accounts/accounts.html', context)

def loginUser(request):
    if request.method == 'POST':
        userEmail = request.POST.get('email')
        rawPassword = request.POST.get('password')
        user = authenticate(email=userEmail, password=rawPassword)
        if user is not None:
            if user.is_superuser:
                #login(request, user)
                print('superuser')
            elif not user.is_superuser:    
                generalInfo = User.objects.get(email=userEmail)
                if str(generalInfo.usertype) == "Student":
                    print('Students')
                elif str(generalInfo.usertype) == "Guest":
                    print('Guest')
        else:
            return redirect('accounts:login')
    return render(request, 'accounts/login.html')
