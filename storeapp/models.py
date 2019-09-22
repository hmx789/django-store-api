from django.db import models
import uuid

# Create your models here.

class Category(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.TextField()
  description = models.TextField()

class Product(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
  name = models.TextField()
  description = models.TextField()
  price = models.DecimalField(max_digits=8, decimal_places=2)
  size = models.CharField(max_length=50)
  units_in_stock = models.IntegerField()
  units_on_order = models.IntegerField()

class ProductImage(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  location = models.TextField()


