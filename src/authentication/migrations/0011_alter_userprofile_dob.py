# Generated by Django 3.2.7 on 2021-10-04 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20211005_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 10, 5, 2, 4, 10, 704771), null=True),
        ),
    ]
