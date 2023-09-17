from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name="home"),
	path('registration', views.registration, name='registration'),
	path('login', views.login, name='login'),
	path('createevent', views.createevent, name='createevent'),
    path('events', views.events, name='events'),
]