from django.urls import path
from core import views

urlpatterns = [
    path('', views.mostrar_login, name='login'),
    path('pagina/', views.index, name='pagina '),
    path('iniciar-sesion/', views.login2, name='login2'),
]