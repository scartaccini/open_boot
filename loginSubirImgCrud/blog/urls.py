#from django.conf.urls import url
from . import views
from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import re_path

urlpatterns = [
    path('blog/', views.post_list, name='lista_post'),
    path('servicios/', views.servicios, name='servicios'),
    re_path(r'^post/(?P<id_post>[0-9]+)/$', login_required(views.post_detail) , name='ver_post'),
    re_path(r'^post/(?P<id_post>[0-9]+)/edit/$', login_required(views.post_edit), name='edit_post'),
    path('post/new/', login_required(views.post_new), name='post_new'),

    ##el sistema de vista por clase de login y logout viene definido en Djnago
    #path('accounts/login/',LoginView.as_view(template_name='blog/login.html'), name='login'), #login,usa la plantilla login.html
    #en setting(opcional) se puede configurar LOGIN_REDIRECT_URL para que nos redireccione a un html en particualr
    ### la ruta acoounts/login, es porque por defecto login_required nos manda
    #path('logout/',LogoutView.as_view(template_name='blog/logout.html'), name='logout'), #logout, nos manda a index.html y en setting(opcional) LOGOUT_REDIRECT_URL

]