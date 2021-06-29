from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import RegForm
from .models import Uuser



def index(request):
	return render(request, 'main/index.html')

def list_of_station(request):
	return render(request, 'main/list_of_station.html')

#list of station
def gas(request):
	return render(request, 'main/gas.html')

def rjd(request):
	return render(request, 'main/rjd.html')

def vtb(request):
	return render(request, 'main/vtb.html')

def otkritie(request):
	return render(request, 'main/otkritie.html')

def kazan(request):
	return render(request, 'main/kazan.html')

def rostov(request):
	return render(request, 'main/rostov.html')
#end list of station


#class Login(CreateView):
#	template_name = 'main/login.html'

class Regist(CreateView):
	#ccылка на html код регистрации
	template_name = 'main/regist.html'
	#форма связанная с моделью пользователя, новый объект которого мы создаем
	form_class = RegForm
	success_url = reverse_lazy('index')
	#работа с контекстом в фале html и собственно отображения страницы
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context