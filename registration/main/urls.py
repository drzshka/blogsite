from django.contrib import admin
from django.urls import path

from .views import index, Regist, list_of_station, gas, rjd, vtb, otkritie, kazan, rostov

#указываем url пути
urlpatterns = [
	path('regist/', Regist.as_view(), name='regist'),
	path('', index, name='index'),
	path('admin/', admin.site.urls),
	path('list_of_station/', list_of_station, name='list_of_station'),
	path('gas/', gas, name='gas'),
	path('rjd/', rjd, name='rjd'),
	path('vtb/', vtb, name='vtb'),
	path('otkritie/', otkritie, name='otkritie'),
	path('kazan/', kazan, name='kazan'),
	path('rostov/', rostov, name='rostov'),
]