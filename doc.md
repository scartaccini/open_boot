########## RUTAS, TEMPLATES, CONTEXTO, ARCHIVOS ESTATICOS, MODULARIZACION(CREACION DE APPS),CRUD,RELACIONES,POSTGRESQL
-firstProject: url con y sin parametros, vistas usando funciones
-secondProject: templates, contexto, comentarios, acciones para listas,variables en html(with)
-thirdProject: Archivos estaticos(css,imagenes,js)
-fourthProject: Herencia en plantillas, include, enlace, variables with usando include(de un html a otro)
-fiftyProject: Modularizacion(aplicaciones-> django-admin startapp comentarios), modelos,
 manejo de url por aplicacion(crear dentro de la aplicacion urls.py)
-sixtyProject: crear y eliminar en bd
-seventyProject: clave foranea, update, read en la bd,uso de filtros, utilizacion de un fake(para poblar la bd de forma rapida)
pip install django-seed
registrar en settings django_seed
pip install psycopg2-binary
python manage.py seed api --number=15
-eightyProject: relaciones 1 a 1, relaciones N a 1 y N a N
-ninetyProject: configuracion para postgresql usando variables de entorno
es importante que el .env, sobre todo en produccion, no este al alcance. 
En produccion no deberia estar en la carpeta raiz, ejemplo:
-httpdocs
    -index.html
- .env
-tenProject: Proyecto : todas las relaciones son: muchos a uno, CRUD sin usar fomularios
###############
# 1 Employee -> 1 Job       1 Job -> 1 Salary
# 1 Job -> N Employee       1 Salary -> N Job

# 1 Employee -> 1 Place     1 Place -> 1 Location
# 1 Place -> N Employee     1 Location -> N Place

#               1 Location -> 1 Country     
#               1 Country -> N lLocation
####### FORMULARIOS(HTML,USANDO SOLO FORMS, MODELFORM),METODOS(GET Y POST),PERSONALIZAR FORMS(WIDGETS),
####### CONTROLES Y VALIDACIONES EN FORMULARIOS
-elevenProject: Formularios html (puros), GET y POST
-twelveProject: Formularios usando forms.py mediante clases, GET y POST
-thirteenProject: widget (estilo a los formulario)
-fourteenProject: Control (def clean_name)y validacion en formularios , todo en forms.py
-fifteenProject: Formularios usando modelos,modelForm 
-sixteenProject: Formulario usando modelForm y guardando en la BD
############## PANEL DE ADMINISTRACION
-seventeenProject: *Creacion de super usuario(python manage.py createsuperuser)
                    estado de los usuarios: staff(puede acceder al panel de administracion)
                   *Registo de modelos en el panel (en models.py admin.site.register(Product))
##############                   
-eighteenProject: Proyecto total: UNA AGENDA Y UN ADMINISTRADOR DE TAREA

-subirimagen: guardar de archivos en BD (pip install Pillow)
-sistemaDeLogin: sistema de login y control de acceso
-loginSubirImgCrud: Combinacion de subirimagen y sistemaDeLogin
-error 404: Maneja el error 404, no encuentra la url 
la forma más fácil es crear en templates un archivo 404.html y en settings:
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']
-mensajeflash
-vistasclasicasgenericas: Ejm maneja preguntas y respuesta, maneja llave foránea usando _set.all, vistas con clases y vistas genéricas
-condicionCarrera: IMPORTANTE!!!!!
EJEMPLO>
reporter = Reporters.objects.get(name="Tintin") #trae de la bd el objeto con el nombre Tintin
reporter.stories_filed += 1 #le suma 1 al campo stories_filed de Tintin
reporter.save()   #guarda el cambio en la bd
Entoneces: trae el obejto de la bd, lo guarda en memoria(python),lo modificamos(+1) y lo guardamos en bd con el cambio
El problema es que si otro usuario hace la misma consulta puede llegar a tener una inconsistencia
CONDICION DE CARRERA, POR ESO ES IMPORTANTE CONTROLAR ESO USANDO f() EJEMPLO>
from django.db.models import F
reporter = Reporters.objects.get(name="Tintin") 
reporter.stories_filed = F("stories_filed") + 1
reporter.save()
DE ESTA FORMA SE HACE TODO DIRECTO EN LA BD, SIN PASAR POR MEMORIA(PYTHON), EVITANDO INCONSISTENCIA
Si dos subprocesos de Python ejecutan el código del primer ejemplo anterior, un subproceso podría recuperar, incrementar y guardar el valor de un campo después de que el otro haya lo recuperó de la base de datos.
El valor que guarda el segundo subproceso será basado en el valor original; El trabajo del primer hilo se perderá.
F() por lo tanto, puede ofrecer ventajas de rendimiento al:
    conseguir que la base de datos, en lugar de Python, haga el trabajo
    Reducir el número de consultas que requieren algunas operaciones
-contextProcessor(contexto global para todo los templates) 
-manejadorArchivosEstaticos: DE ESTA FORMA SE PUEDE TRABAJAR CON ESTATICOS(CSS,JS) TANTO EN DEBUG COMO NO
pip install whitenoise
agregar en settings en middleware 'whitenoise.middleware.WhiteNoiseMiddleware',
STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = 'static/'
STATICFILES_DIRS = [STATIC_ROOT / "static", '/var/www/static']
crear carpeta static en la raiz

