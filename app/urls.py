from django.urls import path
from . import views  # make sure to import your views

urlpatterns = [
    path('', views.json_editor, name='json_editor'),
]
