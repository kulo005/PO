from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


class ControllerAuth:

    def __init__(self, request):
        self.request = request

    def signupuser(self):
        if self.request.method == 'GET':
            return render(self.request, 'SZM/signUpUser.html', {'form': UserCreationForm()})
        else:
            if self.request.POST['password1'].__eq__(self.request.POST['password2']):
                try:
                    user = User.objects.create_user(self.request.POST['username'], password=self.request.POST['password1'])
                    user.save()
                    login(self.request, user)
                    return redirect('useraction')
                except IntegrityError:
                    return render(self.request, 'SZM/signUpUser.html', {'form': UserCreationForm(),
                                                                    'error': 'That username has already been taken. Please choose a new username'})
            else:
                return render(self.request, 'SZM/signUpUser.html',
                              {'form': UserCreationForm(), 'error': 'Passwords did not match'})

    def loginuser(self):
        if self.request.method == 'GET':
            return render(self.request, 'SZM/loginUser.html', {'form': AuthenticationForm()})
        else:
            user = authenticate(self.request, username=self.request.POST['username'], password=self.request.POST['password'])
            if user is None:
                return render(self.request, 'SZM/loginUser.html',
                              {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
            else:
                login(self.request, user)
                return redirect('currentproducts')

    def logoutuser(self):
        if self.request.method == 'POST':
            logout(self.request)
            return redirect('home')

