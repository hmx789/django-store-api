from django.contrib.auth.models import User, Group
from rest_framework import serializers
from storeapp.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['url','username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'name', 'description']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Product
    depth = 1
    fields = ['id', 'price', 'size', 'units_in_stock', 'units_on_order', 'description', 'category']

class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = ProductImage
    fields = ['id', 'product', 'location']