from django.db import models

# Lists for Choices

TERRAIN_CHOICES = [('Plain','Plain'),('Mountain','Mountain'),('Desert','Desert'),('Forest','Forest'),
                   ('Glacier','Glacier'),('Valley','Valley'),('Ocean','Ocean')]

CLIMATE_CHOICES = [('Hot','Hot'),('Cold','Cold'),('Moderate','Moderate'),('Rainy','Rainy')]

FAMOUS_FOR_CHOICES = [('Scenery','Scenery'),('Wildlife','Wildlife'),('Food','Food'),('Weather','Weather'),
                      ('Night Life','Night Life'),('Monuments','Monuments')]


class Destination(models.Model):

    country = models.CharField(max_length=64)
    name = models.CharField(unique=True,max_length=64)
    terrain_type = models.CharField(max_length=32,choices=TERRAIN_CHOICES,null=True,blank=True)
    climate_type = models.CharField(max_length=32,choices=CLIMATE_CHOICES,null=True,blank=True)
    famous_for = models.CharField(max_length=64,choices=FAMOUS_FOR_CHOICES,null=True,blank=True)

    def __str__(self):
        return f'{self.name}, {self.country}'

class DestinationImage(models.Model):

    image = models.ImageField(upload_to='destination-images')
    is_primary = models.BooleanField(default=False)
    destination = models.ForeignKey(to=Destination,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.destination.name} image'

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

class Deal(models.Model):

    destination = models.ForeignKey(to=Destination,on_delete=models.CASCADE)
    duration = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.destination.name}/{self.duration}days'


