from rest_framework import serializers
from base.models import MenuItem
from django.contrib.auth.models import User
from base.models import Ingredient
from base.models import Order
from base.models import UserInfo


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())
    userinfo = UserInfoSerializer()

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "orders", "userinfo"]


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
