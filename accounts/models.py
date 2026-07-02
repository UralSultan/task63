from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    GENDER_CHOICES = [
        (MALE, 'Мужской'),
        (FEMALE, 'Женский'),
        (OTHER, 'Другое'),
    ]

    email = models.EmailField(unique=True, verbose_name='Адрес почты')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар')
    bio = models.TextField(blank=True, verbose_name='Информация о пользователе')
    phone = models.CharField(max_length=20, blank=True, verbose_name='Номер телефона')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, verbose_name='Пол')
    posts_count = models.PositiveIntegerField(default=0, verbose_name='Количество публикаций')
    following_count = models.PositiveIntegerField(default=0, verbose_name='Количество подписок')
    followers_count = models.PositiveIntegerField(default=0, verbose_name='Количество подписчиков')

    def __str__(self):
        return self.username
