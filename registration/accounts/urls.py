from django.urls import path
 
from .views import SignUpView, profilee
 
urlpatterns = [
	path('signup/', SignUpView.as_view(), name='signup'),
	path('profile/', profilee, name='profile'),
]