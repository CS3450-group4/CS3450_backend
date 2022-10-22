from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
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


@api_view(["GET", "POST", "PUT", "DELETE"])
def ingredient(request, id=""):
    if request.method == "GET":
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PUT":
        try:
            order = Ingredient.objects.get(id=id)
        except Ingredient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        try:
            ingredient = Ingredient.objects.get(id=id)
        except Ingredient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ingredient.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(["GET", "PUT", "DELETE"])
def user(request, id):
    if request.method == "GET":
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == "PUT":
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
