from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import viewsets
from .serializers import *

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows Users to be viewed or edited
  """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows Groups to be viewed or edited
  """
  queryset = Group.objects.all()
  serializer_class = GroupSerializer

class CategoryViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows Products to be viewed or edited
  """
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows Products to be viewed or edited
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows Products to be viewed or edited
  """
  queryset = ProductImage.objects.all()
  serializer_class = ProductImageSerializer
