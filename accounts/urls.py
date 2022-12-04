from django.urls import path

from . import views

urlpatterns = [
    path('signup/clinica', views.signupclinica, name='signup-clinica'),
    path('signup/user', views.signupuser, name='signup-user')
]