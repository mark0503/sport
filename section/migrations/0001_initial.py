# Generated by Django 3.2.1 on 2021-05-07 01:13

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anketa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('types', models.CharField(choices=[('S', 'Секция'), ('M', 'Мероприятие')], max_length=1)),
                ('descriptions', models.CharField(max_length=255)),
                ('time_plan', models.CharField(max_length=255)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('age', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('sity', models.CharField(choices=[('K', 'Кировский'), ('L', 'Ленинский'), ('O', 'Октябрьский'), ('Sv', 'Свердловский'), ('S', 'Советский'), ('Z', 'Центральный')], max_length=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('anketa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='section.anketa')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Apeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('types', models.CharField(choices=[('N', 'Устаревшая информация'), ('C', 'Нецензурная лексика'), ('P', 'Фотографии ненормативного характера'), ('S', 'Свой вариант (с текстовым полем)')], max_length=1)),
                ('text', models.TextField(blank=True)),
                ('anketa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apeal', to='section.anketa')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apeals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
