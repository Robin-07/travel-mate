# Generated by Django 3.2.7 on 2021-09-24 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20210925_0317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
    ]
