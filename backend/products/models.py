from django.db import models
import uuid

# A category for a product - more than one category can be related to a single product.
# This is represented in the database, rather than a model field, because it allows for 
# easier configuration during installation for new users.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    parent_category = models.ForeignKey('self', on_delete=models.PROTECT)

# A individual product - this allows information to be stored on the product itself independent of
# each individual listing of the product.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    description = models.TextField()

# A listing of a product posted by a user.
class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    # TODO: implement account class that can be linked to individual listings
    price_per_unit = models.DecimalField(decimal_places=2, max_digits=6)
    quantity = models.IntegerField()