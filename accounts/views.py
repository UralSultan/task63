from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .models import User
from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно.')
            return redirect('accounts:register')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def index_view(request):
    return render(request, 'accounts/index.html')


def login_view(request):
    context = {}

    if request.method == 'POST':
        login_or_email = request.POST.get('login')
        password = request.POST.get('password')

        username = login_or_email
        user_by_email = User.objects.filter(email=login_or_email).first()
        if user_by_email:
            username = user_by_email.username

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:index')

        context['error'] = 'Неверный логин/email или пароль.'

    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('accounts:login')
