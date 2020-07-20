from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.utils import timezone
from .controller_render import ControllerRender


class ControllerProduct(ControllerRender):

    def __init__(self, request, product_pk=None):
        self.request = request
        self.product_pk = product_pk

    def create_product(self):
        if self.request.method == 'GET':
            return render(self.request, 'SZM/createProduct.html', {'form': ProductForm()})
        else:
            try:
                form = ProductForm(self.request.POST)
                newproduct = form.save(commit=False)
                newproduct.user = self.request.user
                newproduct.save()
                return redirect('currentproducts')
            except ValueError:
                return render(self.request, 'SZM/createProduct.html', {'form':ProductForm(), 'error':'Bad data passed in. Try again.'})

    def current_product(self):
        products = Product.objects.filter(user=self.request.user, datecompleted__isnull=True)
        return render(self.request, 'SZM/currentProducts.html', {'products':products})

    def deleted_products(self):
        products = Product.objects.filter(user=self.request.user, datecompleted__isnull=False).order_by('-datecompleted')
        return render(self.request, 'SZM/deletedProducts.html', {'products':products})

    def view_product(self):
        product = get_object_or_404(Product, pk=self.product_pk, user=self.request.user)
        if self.request.method == 'GET':
            form = ProductForm(instance=product)
            return render(self.request, 'SZM/viewProduct.html', {'product':product, 'form':form})
        else:
            try:
                form = ProductForm(self.request.POST, instance=product)
                form.save()
                return redirect('currentproducts')
            except ValueError:
                return render(self.request, 'SZM/viewProduct.html', {'product':product, 'form':form, 'error':'Bad info'})

    def complete_product(self):
        product = get_object_or_404(Product, pk=self.product_pk, user=self.request.user)
        if self.request.method == 'POST':
            product.datecompleted = timezone.now()
            product.save()
            return redirect('currentproducts')

    def delete_product(self):
        product = get_object_or_404(Product, pk=self.product_pk, user=self.request.user)
        if self.request.method == 'POST':
            product.delete()
            return redirect('currentproducts')