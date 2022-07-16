from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	subject=models.CharField(max_length=100)
	message=models.TextField()

	def __str__(self):
		return self.name

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	address=models.TextField()
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to="profile_pic/",default="")
	usertype=models.CharField(max_length=100,default="user")
	

	def __str__(self):
		return self.fname+" - "+self.lname

class Product(models.Model):
	
	CHOICES1=(
			("men","men"),
			("women","women"),
			("kids","kids"),
		)

	CHOICES2=(
			("s","s"),
			("m","m"),
			("l","l"),
			("xl","xl"),
		)
	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	product_category=models.CharField(max_length=100,choices=CHOICES1)
	product_type=models.CharField(max_length=100)
	product_size=models.CharField(max_length=100,choices=CHOICES2)
	product_price=models.PositiveIntegerField()
	product_desc=models.TextField()
	product_image=models.ImageField(upload_to="product_image/")

	def __str__(self):
		return self.seller.fname+" - "+self.product_category

class Wishlist(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.fname+" - "+self.product.product_category

class Cart(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)
	product_qty=models.PositiveIntegerField(default=1)
	product_price=models.PositiveIntegerField()
	total_price=models.PositiveIntegerField()
	payment_status=models.CharField(max_length=100,default="pending")

	def __str__(self):
		return self.user.fname+" - "+self.product.product_category

class Order(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	net_price=models.PositiveIntegerField()
	date=models.DateTimeField(default=timezone.now)
	stripeToekn=models.CharField(max_length=200)

	def __str__(self):
		return self.user.fname+" - "+str(self.net_price)