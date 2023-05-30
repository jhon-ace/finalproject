from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def LoginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin-page')
        else:
            messages.info(request,'Username or Password is incorrect')

    context = {}
    return render(request,'index.html', context)

def Dashboard(request):

    return render(request,'dashboard.html')

