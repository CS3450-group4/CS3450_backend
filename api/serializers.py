from rest_framework import serializers
from base.models import MenuItem
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
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
        fields = ["authLevel", "balance", "actingLevel", "hoursWorked"]


class UserSerializer(serializers.ModelSerializer):
    userinfo = UserInfoSerializer()

    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name", "userinfo"]
        extra_kwargs = {"password": {"write_only": True}}

    def update(self, instance, validated_data):
        if validated_data.get("userinfo"):
            user_info_data = validated_data.pop("userinfo")
            userInfo = instance.userinfo
            for key, value in user_info_data.items():
                if key == "authLevel":
                    userInfo.authLevel = value
                elif key == "actingLevel":
                    userInfo.actingLevel = value
                elif key == "balance":
                    userInfo.balance = value
                elif key == "hoursWorked":
                    userInfo.balance = value
            userInfo.save()

        if validated_data.get("username"):
            instance.username = validated_data.get("username")
        if validated_data.get("first_name"):
            instance.first_name = validated_data.get("first_name")
        if validated_data.get("last_name"):
            instance.last_name = validated_data.get("last_name")

        instance.save()
        return instance

    def create(self, validated_data):
        userinfo = validated_data.pop("userinfo")
        password = validated_data.pop("password")

        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserInfo.objects.create(user=user, **userinfo)
        return user


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
