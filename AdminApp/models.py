from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    CategoryName=models.CharField(max_length=100,unique=True)
    Description=models.TextField()
    CategoryImage=models.ImageField(upload_to="categories")

    def __str__(self):
        return self.CategoryName

class ProductDb(models.Model):
    Product_Name=models.CharField(max_length=100,unique=True)
    Product_Category=models.CharField(max_length=100)
    Prize=models.IntegerField()
    Description=models.TextField()
    Product_Image=models.ImageField(upload_to="Products")

    def __str__(self):
        return self.Product_Name
