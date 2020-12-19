from django.urls import path
from .views import listaUsuario
from rest_framework.authtoken import views

urlpatterns = [
    path('users/', listaUsuario.as_view(), name='user_list'),
    path('apigenerador/', views.obtain_auth_token),
]
