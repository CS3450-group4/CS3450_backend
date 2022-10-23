from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from base.models import MenuItem
from .serializers import *


class Menu(APIView):
    def get_object_by_name(self, name):
        try:
            return MenuItem.objects.get(name=name)
        except MenuItem.DoesNotExist:
            raise Http404

    def save_object_if_valid(self, serializer, good_status=status.HTTP_200_OK):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=good_status)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, name=""):
        # if _ then get all else get named menuItem
        if not name:
            menuItems = MenuItem.objects.all()
            serializer = MenuItemSerializer(menuItems, many=True)
        else:
            menuItems = MenuItem.objects.get(name=name)
            serializer = MenuItemSerializer(menuItems)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)
        return self.save_object_if_valid(
            serializer, good_status=status.HTTP_201_CREATED
        )

    def put(self, request, name):
        menuItem = self.get_object_by_name(name)
        serializer = MenuItemSerializer(menuItem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        menuItem = self.get_object_by_name(name)
        menuItem.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class Orders(APIView):
    def save_object_if_valid(self, serializer, good_status=status.HTTP_200_OK):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=good_status)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        orders = Order.objects.filter(orderStatus="unfullfilled")
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        return self.save_object_if_valid(
            serializer, good_status=status.HTTP_201_CREATED
        )

    def put(self, request, id):
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, request.data, partial=True)
        return self.save_object_if_valid(serializer)


class Ingredients(APIView):
    def get_object_by_id(self, id):
        try:
            return Ingredient.objects.get(id=id)
        except MenuItem.DoesNotExist:
            raise Http404

    def save_object_if_valid(self, serializer, good_status=status.HTTP_200_OK):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=good_status)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IngredientSerializer(data=request.data)
        return self.save_object_if_valid(
            serializer, good_status=status.HTTP_201_CREATED
        )

    def put(self, request, id):
        ingredient = self.get_object_by_id(id)
        serializer = IngredientSerializer(ingredient, request.data)
        return self.save_object_if_valid(serializer)

    def delete(self, request, id):
        ingredient = self.get_object_by_id(id)
        ingredient.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class Users(APIView):
    def get_object_by_id(self, id):
        try:
            return User.objects.get(id=id)
        except MenuItem.DoesNotExist:
            raise Http404

    def save_object_if_valid(self, serializer, good_status=status.HTTP_200_OK):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=good_status)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        user = self.get_object_by_id(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        user = self.get_object_by_id(id)
        serializer = UserSerializer(user, request.data, partial=True)
        return self.save_object_if_valid(serializer)

    def delete(self, request, id):
        user = self.get_object_by_id(id)
        user.delete()
        return Response(status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        return self.save_object_if_valid(
            serializer, good_status=status.HTTP_201_CREATED
        )
