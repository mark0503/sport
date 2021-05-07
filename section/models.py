from django.db import models
from django.contrib.auth.models import User, UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from django.contrib.auth import get_user_model


class UserProfile(User):
    image = models.ImageField(upload_to='users/', blank=True, null=True)

    objects = UserManager()


dict1 = (
    ('S', 'Секция'),
    ('M', 'Мероприятие'),
)

dict2 = (
    ('K', 'Кировский'),
    ('L', 'Ленинский'),
    ('O', 'Октябрьский'),
    ('Sv', 'Свердловский'),
    ('S', 'Советский'),
    ('Z', 'Центральный'),
)

class Anketa(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    types = models.CharField(max_length=1, choices=dict1)
    descriptions = models.CharField(max_length=255)
    time_plan = models.CharField(max_length=255)
    phone = PhoneNumberField()
    age = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена') 
    sity = models.CharField(max_length=6, choices=dict2)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title[:15]


class Comment(models.Model):
    anketa = models.ForeignKey('Anketa', on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comment')
    text = models.TextField()
    created = models.DateTimeField('date published', auto_now_add=True)


dict3 = (
    ('N', 'Устаревшая информация'),
    ('C', 'Нецензурная лексика'),
    ('P', 'Фотографии ненормативного характера'),
    ('S', 'Свой вариант (с текстовым полем)'),
)

class Apeal(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='apeals')
    anketa = models.ForeignKey('Anketa', on_delete=models.CASCADE,
                             related_name='apeal')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    types = models.CharField(max_length=1, choices=dict3)
    text = models.TextField(blank=True)
    