from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User
from .models import ShippingAddress, Create_Card, ProductReview





class Review(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = '__all__'


class Shipping_Form(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class Create_CardForm(forms.ModelForm):
    class Meta:
        model = Create_Card
        fields = '__all__'


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",  "password1", "password2")

    
