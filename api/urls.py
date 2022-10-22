from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.Menu.as_view(http_method_names=["get", "post"])),
    path(
        "menu/<str:name>/",
        views.Menu.as_view(http_method_names=["get", "delete", "put"]),
    ),
    path("orders/", views.getOrders),
    path("orders/<int:id>/", views.getOrders),
    path("user/", views.createUser),
    path("user/<int:id>/", views.user),
    path("ingredient/", views.ingredient),
    path("ingredient/<int:id>/", views.ingredient),
]
