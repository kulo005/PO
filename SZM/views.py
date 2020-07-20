from django.contrib.auth.decorators import login_required
from .controller_auth import ControllerAuth
from .controller_product import ControllerProduct
from .controller_user import Adult, Child
from django.shortcuts import render, redirect
from .forms import PayForm

def home(request):
    site = ControllerProduct(request)
    return site.render_func(request, 'SZM/home.html')


def signupuser(request):
    site = ControllerAuth(request)
    return site.signupuser()


def loginuser(request):
    site = ControllerAuth(request)
    return site.loginuser()

@login_required
def logoutuser(request):
    site = ControllerAuth(request)
    return site.logoutuser()

@login_required
def createproduct(request):
    site = ControllerProduct(request)
    return site.create_product()

@login_required
def currentproducts(request):
    site = ControllerProduct(request)
    return site.current_product()

@login_required
def deletedproducts(request):
    site = ControllerProduct(request)
    return site.deleted_products()

@login_required
def viewproduct(request, product_pk):
    site = ControllerProduct(request, product_pk)
    return site.view_product()

@login_required
def completeproduct(request, product_pk):
    site = ControllerProduct(request, product_pk)
    return site.complete_product()

@login_required
def deleteproduct(request, product_pk):
    site = ControllerProduct(request, product_pk)
    return site.delete_product()

@login_required
def useraction(request):
    if request.method == 'GET':
        return render(request, 'SZM/userAction.html')
    else:
        return redirect('userpay')

@login_required
def userpay(request):
    if request.method == 'POST':
        form = PayForm(data=request.POST)
        if form.is_valid():
            age = form.cleaned_data['number']
            if age >= 18:
                site = Adult(request, age)
                return site.pay_adult()
            else:
                site = Child(request, age)
                return site.pay_child()
    else:
        return redirect('currentproducts')




