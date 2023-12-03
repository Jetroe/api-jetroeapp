from django.db import models

# Create your models here.
# category: name of category.
class Category(models.Model):
    name = models.CharField(max_length=50)

# product: name, description, price, assigned to category, if category delete - set NULL (None).
# ForeignKey: used to create a link or relationship between two models (database tables).
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

# product_image: linked to what product, if product deleted delete image (CASCADE), set the Imagefield.
class Product_Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
# Offers
class Offering(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount_percentage = models.PositiveIntegerField(default=0)
# Deals
class Deal(models.Model):
    offering = models.OneToOneField(Offering, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
