from django.urls import path 

 

from . import views 

from django.contrib import admin 

from django.urls import include, path 

urlpatterns = [ 

    path('', views.index, name='index'), 
    
    # ex: localhost:8080/polls/5/ 

    path('<int:pregunta_id>/', views.detalle, name='detail'), 

    # ex: localhost:8080/polls/5/results/ 

    path('<int:pregunta_id>/results/', views.resultados, name='results'), 

    # ex: localhost:8080/polls/5/vote/ 

    path('<int:pregunta_id>/vote/', views.votar, name='vote'), 


    path('sum/<int:pregunta_id>/<int:pregunta_id2>/', views.sumar, name='sum'),

    path('rest/<int:pregunta_id>/<int:pregunta_id2>/', views.restar, name='rest'),

    path('mult/<int:pregunta_id>/<int:pregunta_id2>/', views.multiplicar, name='mult'),

] 