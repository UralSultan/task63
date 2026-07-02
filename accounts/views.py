from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import User
from .forms import ProfileEditForm, RegisterForm
from posts.models import Post


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
    posts = Post.objects.all()
    return render(request, 'accounts/index.html', {'posts': posts})


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


@login_required(login_url='accounts:login')
def profile_view(request):
    posts = request.user.posts.all()
    return render(request, 'accounts/profile.html', {'posts': posts})


@login_required(login_url='accounts:login')
def profile_edit_view(request):
    profile_form = ProfileEditForm(instance=request.user)
    password_form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        if 'profile_submit' in request.POST:
            profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Профиль обновлен.')
                return redirect('accounts:profile')

        if 'password_submit' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Пароль изменен.')
                return redirect('accounts:profile')

    return render(request, 'accounts/profile_edit.html', {
        'profile_form': profile_form,
        'password_form': password_form,
    })


@login_required(login_url='accounts:login')
def user_search_view(request):
    query = request.GET.get('q', '')
    users = User.objects.none()

    if query:
        users = User.objects.filter(
            Q(username__icontains=query) |
            Q(email__icontains=query) |
            Q(first_name__icontains=query)
        )

    return render(request, 'accounts/user_search.html', {
        'query': query,
        'users': users,
    })


@login_required(login_url='accounts:login')
def user_profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    return render(request, 'accounts/user_profile.html', {'profile_user': profile_user})


@login_required(login_url='accounts:login')
def user_posts_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    posts = profile_user.posts.all()
    return render(request, 'accounts/user_posts.html', {
        'profile_user': profile_user,
        'posts': posts,
    })
