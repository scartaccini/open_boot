* crear entorno virtual (python -m venv web)
* activar entorno
* instalar django (pip install django)
* crear proyecto en django(django-admin startproject proyectoweb)
* agregar carpeta proyectoweb al ide
  ficheros: manage.py (sirve para gestionar todo nuestro proyecto desde la termina)
            urls.py (para registrar las urls a usar)
            settings.py (contiene la configuración)
            wsgi.py (tiene la información para desplegar el proyecto en producción)
* sincronizar base de datos sqlite3 que trae por defecto (python manage.py migrate)
* en caso de ser necesario, crear una app (django-admin startapp nucleo) SI VAMOS A USAR BD SI O SI
  el uso de crear apps sirve para organizar el proyecto, un proyecto puede tener muchas apps y una app puede estar en muchos proyectos, se puede reutilizar
* en el settings agregamos la app nucleo (
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'nucleo'
]
)  
* en la carpeta nucleo creamos urls.py (
    from . import views
    urlpatterns = [
    path('', views.home, name="home"),
    
    ]
    )
* incluimos urls de la app nucleo en el urls.py gral, el del proyecto( 
    from django.urls import include, path
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('nucleo/', include('nucleo.urls'))
]
)
* en el fichero nucleo/views.py crear la función home
* crear carpeta templates en la raiz del proyecto y en setting.py(
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
   )
* dentro de la carpeta templates podemos crear otra con el nombre de la app(templates/nucleo)
* si manejamos archivos estáticos(js, css, img), crear en la raiz del proyecto carpeta static
* en el settings.py (
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [BASE_DIR / "static", '/var/www/static']
    ) 
* en los html que necesitemos contenido estático hay que cargar({% load static %}) y luego podemos acceder por ejemplo a una img ({% static 'img/contact-bg.jpg' %})  

**********
* si necesitamos manipular imagenes entonces importaremos Pillow (pip install Pillow)
* en caso de necesitar un modelo en la app nucleo para mapear con la bd, nucleo/models.py (
    from django.db import models

    class Project(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        image = models.ImageField()
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
    )
* cada vez que hagamos un cambio en nuestro ficheros models.py ejecutaremos estos dos comandos para crear una migración y posteriormente aplicarla (python manage.py makemigrations python manage.py migrate)
* En settings: MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
* En url principal: urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
* En views  en el modelform agregar request.FLES:
form = GrafitiForm(request.POST, request.FILES)
* En el formulario html para guardar : <form action="" method="post" enctype="multipart/form-data">
* En el html para mostrar: <img src="{{lista_grafitis.imagen.url}}" width="200" height="200">
