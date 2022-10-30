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

    def update(self, instance, validated_data):
        if validated_data.get("userinfo"):
            user_info_data = validated_data.pop("userinfo")
            userInfo = instance.userinfo
            if user_info_data.get("authLevel"):
                userInfo.authLevel = user_info_data.get("authLevel")

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


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
