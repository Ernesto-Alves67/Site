from django.urls import path
from folio import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edu', views.educacao),
    path('xp', views.experiencia, name='xp'),
    path('skills', views.skills, name='skills'),
    path('interesses', views.interesses, name='interesses'),
    path('projetos', views.projects, name='projetos'),
]
