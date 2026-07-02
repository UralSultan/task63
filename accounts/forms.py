from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'avatar',
            'password1',
            'password2',
            'first_name',
            'bio',
            'phone',
            'gender',
        ]
        labels = {
            'username': 'Логин',
            'email': 'Адрес почты',
            'avatar': 'Аватар',
            'first_name': 'Имя',
            'bio': 'Информация о пользователе',
            'phone': 'Номер телефона',
            'gender': 'Пол',
        }
        help_texts = {
            'username': '',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['avatar'].required = True
        self.fields['email'].required = True
