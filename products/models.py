from django.db import models

from users.models import User

class Menu(models.Model):
    name = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name    = models.CharField(max_length=10)
    menu    = models.ForeignKey("Menu", on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'categories'

class Product(models.Model):
    menu                = models.ForeignKey("Menu", on_delete=models.CASCADE)
    category            = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    name                = models.CharField(max_length=100)
    price               = models.DecimalField(max_digits=9 , decimal_places=2)
    thumbnail_image_url = models.CharField(max_length=1000)
    description         = models.CharField(max_length=500)
    product_hits        = models.IntegerField()
    created_at          = models.DateTimeField(auto_now_add = True)
    updated_at          = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'products'

class Image(models.Model):
    product    = models.ForeignKey("Product", on_delete=models.CASCADE)
    image_url  = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'images'

class TastingNote(models.Model):
    product    = models.ForeignKey("Product", on_delete=models.CASCADE)
    name       = models.CharField(max_length=20)

    class Meta:
        db_table = 'tasting_notes'

class ProductStock(models.Model):
    product    = models.ForeignKey("Product", on_delete=models.CASCADE)
    stock      = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'product_stocks'

class Cart(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    product    = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity   = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'carts'
