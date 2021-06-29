# Generated by Django 3.1.2 on 2021-06-29 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя пользователя')),
                ('e_mail', models.CharField(max_length=30, verbose_name='Электронная почта')),
                ('password', models.CharField(max_length=32, verbose_name='Пароль')),
            ],
        ),
    ]
