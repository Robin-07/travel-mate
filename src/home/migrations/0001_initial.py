# Generated by Django 3.2.7 on 2021-10-03 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('terrain_type', models.CharField(choices=[('Plain', 'Plain'), ('Mountain', 'Mountain'), ('Desert', 'Desert'), ('Forest', 'Forest'), ('Glacier', 'Glacier'), ('Valley', 'Valley'), ('Ocean', 'Ocean')], max_length=32)),
                ('climate_type', models.CharField(choices=[('Hot', 'Hot'), ('Cold', 'Cold'), ('Moderate', 'Moderate'), ('Rainy', 'Rainy')], max_length=32)),
                ('famous_for', models.CharField(choices=[('Food', 'Food'), ('Weather', 'Weather'), ('Night Life', 'Night Life')], max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='DestinationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='destination-images')),
                ('Destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.destination')),
            ],
        ),
    ]