# Generated by Django 3.0.6 on 2020-06-11 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SZM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mydate',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 11, 16, 51, 26, 109500)),
        ),
    ]