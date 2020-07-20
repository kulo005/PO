from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Product, ProductAdmin)
