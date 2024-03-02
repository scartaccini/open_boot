from django.urls import path

from . import views
from . import views2
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
 
    path("consultar/<int:question_id>/", views2.detail, name="detail2"),
]