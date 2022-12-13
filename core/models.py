
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.

class User(AbstractUser):
    mobilenumber = models.CharField(max_length=10, null=True)
    address=models.CharField(max_length=100,null=True)
    uimg = models.ImageField(upload_to='ProfilePic/',default='profilepic.png')
    t = [(1,'Guest'),(2,'Wholesaler'),(3,'Retailer')]
    role = models.IntegerField(choices=t,default=1)

class Rolereq(models.Model):
    f = [(2,'Wholesaler'),(3,'Retailer')]
    rltype = models.IntegerField(choices = f)
    pfe = models.ImageField(upload_to='ID_Prf/',default='profilepic.png')
    is_checked = models.BooleanField(default=False)
    uname = models.CharField(max_length=50)
    ud = models.OneToOneField(User, on_delete=models.CASCADE)

class Products(models.Model):
    pno = models.IntegerField()
    pname = models.CharField(max_length=200)
    pcost = models.DecimalField(max_digits=10, decimal_places=2)
    pimg = models.ImageField(upload_to = 'Products/',default = 'profilepic.png')
    wid = models.ForeignKey(User,on_delete=models.CASCADE)

class Cart(models.Model):
    pid=models.IntegerField(default=None)
    pname = models.CharField(max_length=200,default=None)
    pcost = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    uid=models.ForeignKey(User,on_delete=models.CASCADE)
    quant=models.IntegerField()
    proid=models.ForeignKey(Products,on_delete=models.CASCADE,default=None)
    is_bought=models.BooleanField(default=False)