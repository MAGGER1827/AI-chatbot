
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('bot_search/', views.bot_search, name='bot_search')
   ]
