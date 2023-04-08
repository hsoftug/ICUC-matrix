from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission



class Category(models.Model):
    Category_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name_plural="Categories"

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    Order_id=models.AutoField(primary_key=True)
    User_id=models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.first_name

class OrderItem(models.Model):
    OrderItem_id=models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.category_name

class Cart(models.Model):
    Cart_id=models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.user.username}'s Cart Item: {self.product.name} ({self.quantity})"

class User(AbstractUser):
    User_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    is_customer = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='naana_users')
    user_permissions = models.ManyToManyField(Permission, related_name='naana_users_permissions')
    def __str__(self):
        return self.username