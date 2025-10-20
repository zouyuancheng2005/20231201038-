from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('admin/', admin.site.urls),
]