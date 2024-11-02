from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serlializers import ItemSerlializer, UserSerlializer
from .models import Item
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(api_urls)

@api_view(['POST'])
def add_items(request):
    item = ItemSerlializer(data= request.data)
    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('Item Already exists')
    if item.is_valid():
        item.save()
        return Response(item.data)
    else : 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def view_items(request):
    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else :
        items = Item.objects.all()
    
    if items : 
        serialiazer = ItemSerlializer(items, many=True)
        return Response(serialiazer.data)
    else :
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    serializer = ItemSerlializer(item)
    return Response(serializer.data)

@api_view(['POST'])
def update_item(request, pk):
    item = Item.objects.get(pk=pk)
    data = ItemSerlializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else :
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

@api_view(['POST'])
def signup(request):
    serializer = UserSerlializer(data=request.data)
    if serializer.is_valid():
        user = User(
            username=serializer.validated_data['username'],
            email=serializer.validated_data.get('email', '')
        )
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)

        user_data = serializer.data
        user_data.pop('password', None)

        return Response({"user":user_data, "token":token.key})
    else :
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)