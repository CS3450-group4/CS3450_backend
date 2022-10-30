from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from base.models import MenuItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import *

"""
create login api endpoint
check request.username and reqest.password
authenticat with django.contrib.auth.authenticate
if auth then dango.contrib.auth.login


make logout endpoint
"""


class Login(APIView):
    def post(self, request):
        if "username" in request.data and "password" in request.data:
            username = request.data["username"]
            password = request.data["password"]
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # TODO: send 401 if not auth
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response()


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
        user = authenticate(request, username="jimbo", password="testpass")
        if user is not None:
            login(request, user)
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


@api_view(["GET"])
def getUserInfo(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    info = UserInfo.objects.get(user=user)
    serializer = UserInfoSerializer(info)
    return Response(serializer.data)


@api_view(["GET"])
def getAllUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getUserByEmail(request, name):
    try:
        user = User.objects.get(userName=name)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    seralizer = UserSerializer(user)
    return Response(seralizer.data)
