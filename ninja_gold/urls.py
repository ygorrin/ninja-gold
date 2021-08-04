
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', include('process_money.urls')),
    path('admin/', admin.site.urls),
]
