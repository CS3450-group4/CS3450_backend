from django.urls import path
from . import views

urlpatterns = [
        path('', views.getProducts),
        path('additem', views.addMenuItem),
        ]
