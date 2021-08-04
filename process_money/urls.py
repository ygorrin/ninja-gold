from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('process_money', views.process_money),
    #path('second/<name>', views.second)
]
