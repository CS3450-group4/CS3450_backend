from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import MenuItem
from .serializers import *


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def menu(request, name=''):
    if request.method == 'GET':
        menuItems = MenuItem.objects.all()
        serializer = MenuItemSerializer(menuItems, many=True)
        return Response(serializer.data,
                status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                    status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            menuItem = MenuItem.objects.get(name=name)
        except MenuItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        menuItem.delete()
        return Response(status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        try:
            menuItem = MenuItem.objects.get(name=name)
        except MenuItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MenuItemSerializer(menuItem,
                data=request.data)
        if serializer.is_valid():
           serializer.save() 
           return Response(serializer.data)
        return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT'])
def getOrders(request, id=''):
    if request.method == 'GET':
        orders = Order.objects.filter(orderStatus='unfullfilled')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                    status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            order = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, request.data,
                partial=True)
        if serializer.is_valid():
           serializer.save() 
           return Response(serializer.data)
        return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ingredient(request, id=''):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IngredientSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                    status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'PUT':
        try:
            order = Ingredient.objects.get(id=id)
        except Ingredient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(order, request.data)
        if serializer.is_valid():
           serializer.save() 
           return Response(serializer.data)
        return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            ingredient = Ingredient.objects.get(id=id)
        except Ingredient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ingredient.delete()
        return Response(status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def user(request, id):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user, request.data, partial=True)
        if serializer.is_valid():
           serializer.save() 
           return Response(serializer.data)
        return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,
                status=status.HTTP_201_CREATED)
    return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getAllUsers(request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
