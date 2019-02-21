from django.shortcuts import render

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import (login as auth_login,  authenticate)
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from home_site.models import Country,City
from reservation.models import car,hotel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form2 = ImgForm(request.POST)
        if form.is_valid() and form2.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                #raw_id = form.cleaned_data.get('id')
                #form2 = ImgForm(initial={'user_id': raw_id})
                img = request.POST.get('user_img')
                user = authenticate(username=username, password=raw_password)
                customuser = User_custom(user_img=img, user_id=user.id)
                request.session['user_id']=user.id
                customuser.save()
                auth_login(request, user)

                #form2.save()
                return redirect('/user/profile')
    else:
        form = SignUpForm()
        form2 =ImgForm()
    return render(request, 'signup.html', {'form': form, 'form2': form2})


def login(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        print(request.user.id)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'login.html', context)


def user_data(request):
    if request.user.is_authenticated():
        countries = Country.objects.all()
        username = request.user.username
        email = request.user.email
        visit = request.user.last_login
        date = request.user.date_joined
        id = request.user.id
        img=User_custom.objects.filter(user_id=request.user.id)
        cars = car.objects.filter(user_id=id).values(
            'from_date',
            'location__sight_name',  # Equal to bug.priority.value
            'destination__sight_name',
            'to_date',
            'from_time',
            'to_time',
            'city__city_name',
            'country__country_name'
        )

        hotels = hotel.objects.filter(user_id=id).values(
            'from_date',
            'hotels__hotel_name',  # Equal to bug.priority.value
            'to_date',
            'person_number',
            'city__city_name',
            'country__country_name'
        )
        context = {'username': username, 'email':email,
                   'count':countries, 'date_joined': date, 'last_visit': visit , 'user_img':img ,'id':id,
                   'hotels':hotels,'cars':cars}
       # request.sesssion['id']=id

        return render(request, 'profile.html', context)


def user_logout(request):
    logout(request)
    return redirect('/home_site')




def edit(request):
    if request.method == 'POST':
        form = EditForm(request.POST, instance=request.user)
        form2 = ImgFormEdit(request.POST, instance=request.user)

        if form.is_valid() and form2.is_valid():
                form.save()
                _username = request.POST['username']
                _password = request.POST['password1']
                user = authenticate(username=_username, password=_password)
                auth_login(request, user)
                #raw_id = form.cleaned_data.get('id')
                #form2 = ImgForm(initial={'user_id': raw_id})
                img = request.POST.get('user_img')
                customuser=User_custom.objects.get(user_id=user.id)
                customuser.user_img=img
                customuser.save()


                #form2.save()
                return redirect('/user/profile')
    else:
        form = EditForm()
        form2 =ImgFormEdit()
    return render(request, 'edit.html', {'form': form ,'form2':form2})