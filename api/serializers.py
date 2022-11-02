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
        fields = ["authLevel", "balance", "actingLevel", "hoursWorked"]


class UserSerializer(serializers.ModelSerializer):
    userinfo = UserInfoSerializer()

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "userinfo"]

    def update(self, instance, validated_data):
        if validated_data.get("userinfo"):
            user_info_data = validated_data.pop("userinfo")
            userInfo = instance.userinfo

            if user_info_data.get("authLevel"):
                userInfo.authLevel = user_info_data.get("authLevel")
            if user_info_data.get("actingLevel"):
                userInfo.actingLevel = user_info_data.get("actingLevel")
            if user_info_data.get("balance"):
                userInfo.balance = user_info_data.get("balance")
            if user_info_data.get("hoursWorked"):
                userInfo.hoursWorked = user_info_data.get("hoursWorked")

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
        user = User.objects.create(**validated_data)
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
