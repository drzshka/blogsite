from django.forms import ModelForm

from .models import Uuser

class RegForm(ModelForm):
	class Meta:
		model = Uuser
		fields = ('name', 'e_mail', 'password')