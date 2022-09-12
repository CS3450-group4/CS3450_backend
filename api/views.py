from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import MenuItem
from .serializers import MenuItemSerializer


@api_view(['GET'])
def getProducts(request):
    menuItems = MenuItem.objects.all()
    serializer = MenuItemSerializer(menuItems, many=True)
    return Response({"items": serializer.data})

@api_view(['POST'])
def addMenuItem(request):
    serializer = MenuItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
