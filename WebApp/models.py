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