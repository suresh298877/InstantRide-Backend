# accounts/views.py
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from rest_framework import status


@login_required(login_url='login')
def home(request):
    return HttpResponse("home page")


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Hash the password
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to a success page
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


# users/views.py

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page after login
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


class ApiCreateUser(APIView):
    def post(self, request, format=None):
        serializer = serializers.CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
