from django.shortcuts import render, redirect, get_object_or_404
from .forms import PayForm
from .models import Product
from .controller_pay import ChildPaySystem, AdultPaySystem


class Child():

    def __init__(self, request, age):
        self.request = request
        self.age = age
        self.pay = ChildPaySystem.calculate_pay(self.age)

    def pay_child(self):
        if self.age <= 15:
            pay = int(ChildPaySystem.calculate_relief(self.pay))
            return render(self.request, 'SZM/pay.html', {'pay': pay})
        else:
            return render(self.request, 'SZM/pay.html', {'pay': self.pay})

class Adult():

    def __init__(self, request, age):
        self.request = request
        self.age = age
        self.pay = AdultPaySystem.calculate_pay(self.age)

    def pay_adult(self):
        if self.age >= 50:
            pay = int(AdultPaySystem.calculate_relief(self.pay))
            return render(self.request, 'SZM/pay.html', {'pay': pay})
        else:
            return render(self.request, 'SZM/pay.html', {'pay': self.pay})

