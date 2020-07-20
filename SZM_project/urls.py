"""SZM_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SZM import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    # Products
    path('', views.home, name='home'),
    path('current/', views.currentproducts, name='currentproducts'),
    path('create/', views.createproduct, name='createproduct'),
    path('product/<int:product_pk>', views.viewproduct, name='viewproduct'),
    path('product/<int:product_pk>/delete', views.deleteproduct, name='deleteproduct'),
    path('useraction/', views.useraction, name='useraction'),
    path('userpay/', views.userpay, name='userpay'),
]
