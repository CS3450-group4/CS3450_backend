from django.urls import path
from . import views

urlpatterns = [
        path('menu/', views.menu),
        path('menu/<str:name>/', views.menu),
        path('orders/', views.getOrders),
        path('orders/<int:id>/', views.getOrders),
        path('user/', views.createUser),
        path('user/all', views.getAllUsers),
        path('userName/<str:name>/', views.getUserByEmail),
        path('user/<int:id>/', views.user),
        path('ingredient/', views.ingredient),
        path('ingredient/<int:id>/', views.ingredient),
        ]
