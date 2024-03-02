* pip install django-bootstrap-v5
* en settings, INSTALLED_APPS AGREGAR 'bootstrap5',
* en el o los htmls, entre el head agregar:
    {% load bootstrap5 %}
    {% bootstrap_css %}
    {% bootstrap_javascript %}