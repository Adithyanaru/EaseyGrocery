from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Name=models.CharField(max_length=100,blank=True,null=True)
    Email=models.EmailField(blank=True,null=True)
    Message=models.TextField(blank=True,null=True)

class AccountDb(models.Model):
    Username=models.CharField(max_length=100,blank=True,null=True)
    Email=models.EmailField(blank=True,null=True)
    Password=models.CharField(max_length=100,blank=True,null=True)
    Confrom_Password = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.Email
class  CartDb(models.Model):
    # Username=models.CharField(max_length=100,blank=True,null=True)
    Username = models.CharField(max_length=100, default="")
    ProductName=models.CharField(max_length=100,blank=True,null=True)
    Quantity=models.IntegerField(blank=True,null=True)
    Price=models.IntegerField(blank=True,null=True)
    Total_Price=models.IntegerField(blank=True,null=True)
    Product_Image=models.ImageField(upload_to='Cart_img',blank=True,null=True)

