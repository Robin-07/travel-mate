from django.contrib.auth.models import AbstractUser
from django.db import models
from django import utils


class User(AbstractUser):

    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile-images', default='default-profile-image.png')
    phone = models.CharField(max_length=10, default="", null=True, blank=True)
    dob = models.DateField(default=utils.timezone.now, null=True, blank=True)

    def __str__(self):
        return self.user.email

    @property
    def image_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

