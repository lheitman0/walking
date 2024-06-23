from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/', views.info_handler, name='info_handler'),
    path('route/', views.route_generator, name='route_generator'),
]