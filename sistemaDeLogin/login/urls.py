
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import SignUpView,UpdatePassUsuario

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('index/', views.index, name='index'),
    path('prueba/', login_required(views.prueba), name='prueba'),
    path('', views.home, name='home'),
    path('registrarme/', SignUpView.as_view(), name='registrar_usuario'),
    #path(r'^modpass/(?P<pk>\d+)/$',login_required(UpdatePassUsuario.as_view()), name='modificarDatosUsu'),
    path('modificar/<int:pk>',login_required(UpdatePassUsuario.as_view()), name='modificarDatosUsu'),
]