from django.urls import path

from . import views

app_name = 'clinica'
urlpatterns = [
    path('', views.home, name='home'),
    path('home/search/', views.search, name='search'),
    path('home/<int:id>/', views.medico, name='medico'),
    path('home/especialidade/<int:especialidade_id>/',
         views.especialidade, name='especialidade'),

]
