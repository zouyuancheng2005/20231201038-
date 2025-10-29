from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('section1/', views.section1, name='section1'),
    path('section2/', views.section2, name='section2'),
    path('section3/', views.section3, name='section3'),
]