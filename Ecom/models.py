from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField()
    discount_offer = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    storage = models.CharField(max_length=200)
    discription = models.TextField()
    discount_price = models.IntegerField()
    price = models.IntegerField()
    trending = models.BooleanField(default=False)

    def __str__(self):
        return self.name




class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='upload', null=True)

    def __str__(self):
        return self.product.name


class Carousel(models.Model):
    image = models.ImageField(upload_to='upload', null=True)
    title = models.CharField(max_length=200)
    discription = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    review = models.CharField(max_length=150)
    rating = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class CheckoutCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    total = models.IntegerField(default=0, null=True, blank=True)


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    comp_name = models.CharField(max_length=255, null=True, blank=True)
    area_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    busines_address = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Create_Card(models.Model):
    name = models.CharField(max_length=30)
    card_number = models.IntegerField()
    exp_year = models.CharField(max_length=30)
    exp_month = models.CharField(max_length=30)
    CSV = models.IntegerField()

    def __str__(self):
        return self.name
