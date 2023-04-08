from django.contrib import admin
from .models import *

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'category_id', 'price')
    list_filter = ('category_id', 'name')
    search_fields = ('name', 'category_id')

class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'product_id','First_name', 'Date')
    list_filter = ('First_name', 'Date')
    search_fields = ('product_id', 'Date')

class UserAdmin(admin.ModelAdmin):
    list_display = ( 'User_id','Username', 'Email')
    list_filter = ('First_name', 'Username')
    search_fields = ('User_id', 'Username')

class OrderitemAdmin(admin.ModelAdmin):
    list_display = ( 'Order_id','product_id', 'price')
    list_filter = ('Order_id', 'price')
    search_fields = ('product_id', 'Order_id')

class CartAdmin(admin.ModelAdmin):
    list_display = ( 'product_id','user_id', 'Cart_id')
    list_filter = ('Cart_id', 'user_id')
    search_fields = ('product_id', 'Cart_id')    
    
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(OrderItem)
admin.site.register(Cart)
