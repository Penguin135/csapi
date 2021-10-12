from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from login.forms import UserForm

def index(request):
    return HttpResponse('login 페이지입니다')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')

            # user authentication
            user = authenticate(username=username, password=password1)

            # login
            login(request, user)
            return redirect('/api/')
    else:
        form = UserForm()
    return render(request, 'login/signup.html', {'form' : form})
