from django.urls import path

from . import views


# Create URL patterns here.
urlpatterns = [
    path('', views.the_program, name='martial_arts'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('apply/', views.apply, name='apply'),
]