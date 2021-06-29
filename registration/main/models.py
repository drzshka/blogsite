from django.db import models

class Uuser(models.Model):
	#логин
	name = models.CharField(max_length=30, verbose_name='Имя пользователя')
	#почта
	e_mail = models.CharField(max_length=30, verbose_name='Электронная почта')
	#пароль
	password = models.CharField(max_length=32, verbose_name='Пароль')
