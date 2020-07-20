from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Product(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mydate = models.DateTimeField(default=datetime.now())


    def __str__(self):
        return self.title
