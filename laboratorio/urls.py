from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'laboratorio'

urlpatterns = [
    path('', views.home, name='home'),
    path('laboratorio/', views.laboratorio, name='laboratorio'),
    path('mostrar/', views.mostrar_laboratorios, name='mostrar'),
    path('insertar/', views.insertar_laboratorio, name='insertar'),
    path('editar/<int:laboratorio_id>/', views.editar_laboratorio, name='editar_laboratorio'),
    path('eliminar/<int:laboratorio_id>/', views.eliminar_laboratorio, name='eliminar'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
  
]
