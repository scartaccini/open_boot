from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import re_path
urlpatterns = [
    path('registrarme/', views.SignUpView.as_view(), name='registrar_usuario'),
    ##el sistema de vista por clase de login y logout viene definido en Djnago
    path('accounts/login/', LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    re_path(r'^mod_usuario/(?P<pk>\d+)/$',login_required(views.UpdatePassUsuario.as_view()), name='mod_usuario'),
    path('', views.inicio, name='inicio'),
   
]