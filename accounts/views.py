from django.contrib import messages
from django.shortcuts import redirect, render

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
