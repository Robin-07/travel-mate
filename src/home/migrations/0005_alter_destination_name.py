# Generated by Django 3.2.7 on 2021-10-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_deal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]