from django.urls import path

from . import views
from . import views2
from . import views3


urlpatterns = [
    #path("", views.index, name="index"),
    #path("<int:question_id>/", views.detail, name="detail"), 
    #path("consultar/<int:question_id>/", views2.detail, name="detail2"),
    #path("<int:question_id>/vote/", views.vote, name="vote"),
    ################vistas basadas en clase
    path("", views3.IndexView.as_view(), name="index"),
    path("<int:pk>/", views3.DetailView.as_view(), name="detail"),
    path("detalle2/<int:pk>/", views3.DetailView2.as_view(), name="detail2"),
    path("<int:pk>/results/", views3.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views3.vote, name="vote"),
]