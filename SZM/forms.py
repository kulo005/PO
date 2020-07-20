from django.forms import ModelForm
from .models import Product
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'info']


class PayForm(forms.Form):
    number = forms.IntegerField()