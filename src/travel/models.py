from django.db import models
from home.models import Package
from authentication.models import User
# Create your models here.

class Booking(models.Model):
    package = models.ForeignKey(Package, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}'
