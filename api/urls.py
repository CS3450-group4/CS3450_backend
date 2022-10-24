from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.Menu.as_view(http_method_names=["get", "post"])),
    path(
        "menu/<str:name>/",
        views.Menu.as_view(http_method_names=["get", "delete", "put"]),
    ),
    path("orders/", views.Orders.as_view(http_method_names=["get", "post"])),
    path("orders/<int:id>/", views.Orders.as_view(http_method_names=["put"])),
    path("user/", views.Users.as_view(http_method_names=["post"])),
    path(
        "user/<int:id>/",
        views.Users.as_view(http_method_names=["get", "put", "delete"]),
    ),
    path("ingredient/", views.Ingredients.as_view(http_method_names=["get", "post"])),
    path(
        "ingredient/<int:id>/",
        views.Ingredients.as_view(http_method_names=["put", "delete"]),
    ),
    path("login/", views.Login.as_view(http_method_names=["post"])),
    path("logout/", views.Logout.as_view(http_method_names=["post"])),
]
