from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('process_money/', views.index),
    path('crear_datos/', views.crear_datos),
    path('vaciar_datos/', views.vaciar_datos),
]
