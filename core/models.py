from email.policy import default
from django.db import models
from datetime import datetime    

from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    slug = models.CharField(max_length=100)
    desc = models.TextField(max_length=4000)
    price = models.IntegerField(max_length=30)
    img = models.ImageField(upload_to = "productImg")
    date = models.DateTimeField(default=datetime.now(), blank=True)
    tire_size = models.IntegerField(max_length=100,default=0)
    vehicle = models.CharField(max_length=100,default="")

    def __str__(self) -> str:
        return self.title
class Addres(models.Model):
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   name= models.CharField(max_length=200)
   address = models.CharField(max_length=200,default="")
   address2 = models.CharField(max_length=200,default="")
   city= models.CharField(max_length=200)
   zipcode= models.IntegerField()
   state=models.CharField(max_length=100)

   def __str__(self) -> str:
      return self.name



class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1,)
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self) -> str:
       return str(self.id)

    @property
    def total_coast(self):
        return self.quantity * self.product.price


ORDER_STATUS=(
    ("Pending","Pending"),
    ("Delevired","Delevired"),
    ("On The Way","On The Way"),
    ("Packed","Packed"),
    ("Cancel","Cancel"),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    costumer = models.ForeignKey(Addres,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=ORDER_STATUS,default="Pending",max_length=100)

    def __str__(self) -> str:
       return str(self.id)
    @property
    def total_coast(self):
        return self.quantity * self.product.price
   
   



class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=3000)
    Date = models.DateField(default=datetime.now())
    

    def __str__(self) -> str:
        return self.fullname
     
class ProductReview(models.Model):
    id = models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Product, on_delete=models.CASCADE)
    Date = models.DateField(default=datetime.now())

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username