from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Import Category from main.models
from main.models import Category

class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(null=True,blank=True)
    big_image = models.ImageField(null=True,blank=True)
    description = models.CharField(max_length=1000, default="Company")
    page_description = models.CharField(max_length=1000, default="undefined")
    alt_tag = models.CharField(max_length=50, default="undefined")
    metatags = models.CharField(max_length=1000, default="undefined")
    created = models.DateTimeField(default=timezone.now, null=True, blank=True)
    readonly_fields = ('created',)

    def __str__(self):
        return str(self.id)+' '+str(self.name)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone = models.CharField(max_length=10,null=True, blank=True)
    categories = models.ManyToManyField(Category)
    balance = models.FloatField()
    referral_code = models.CharField(max_length=15,null=True, blank=True)
    referee_code = models.CharField(max_length=15,null=True, blank=True)
    account_name = models.CharField(max_length=100,null=True, blank=True)
    account_no =  models.CharField(max_length=50,null=True, blank=True)
    ifsc = models.CharField(max_length=15,null=True, blank=True)
    paytm_name = models.CharField(max_length=100,null=True, blank=True)
    paytm_no = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, null=True, blank=True)
    readonly_fields = ('created',)

    def __str__(self):
        return str(self.id)+' '+str(self.user.username)

class Department(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)+" "+self.name  

class Item(models.Model):
    name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)+" "+self.name    


class Buy(models.Model):
    user = models.ForeignKey(Customer)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user.username+" "+self.item.name

class Cart(models.Model):
    user = models.ForeignKey(Customer)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.user.username+" "+self.item.name



class Viewhistory(models.Model):
    user = models.ForeignKey(Customer)
    item = models.IntegerField()

    def __str__(self):
        return self.user.user.username+" "+str(self.item)
