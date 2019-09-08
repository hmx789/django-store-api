from django.db import models
import uuid

# Create your models here.
# still need to make migrations

class Category(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.TextField()
  description = models.TextField()
  
class ProductDetails(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
  name = models.TextField()
  description = models.TextField()

class Product(models.Model); 
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  product_details_id = models.ForeignKey(ProductDetails, on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  size = models.CharField(max_length=50)
  units_in_stock = models.IntegerField()
  units_on_order = models.IntegerField()

class ProductImage(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
  location = models.TextField()


