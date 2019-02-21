from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import *


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form2 = ImgForm(request.POST)
        if form.is_valid() and form2.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                form2.save()
                return redirect('/home_site')
    else:
        form = SignUpForm()
        form2 =ImgForm()
    return render(request, 'signup.html', {'form': form, 'form2': form2})
