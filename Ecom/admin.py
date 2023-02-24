from django.contrib import admin
from .models import Category, Company, Image, Carousel, Product, CheckoutCart, ShippingAddress, Create_Card

# Register your models here.
admin.site.register(CheckoutCart)
admin.site.register(ShippingAddress)
admin.site.register(Create_Card)


# admin.site.register(User)

# Company Model
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Company, CompanyAdmin)


# Product Model
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'company', 'category', 'picture', 'discount_offer', 'name', 'storage', 'discription', 'price', 'discount_price',
        'trending')


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)

# Image Model
class ImageAdmin(admin.ModelAdmin):
    list_display = ('picture', 'product')


admin.site.register(Image, ImageAdmin)
