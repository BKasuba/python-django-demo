from django.db import models

class Transmission(models.TextChoices):
    AUTO = 'AUTO', 'Automatic'
    MANUAL = 'MANUAL', 'Manual'

class Cars(models.Model):
    full_name = models.CharField(max_length=100, blank=False)
    brand = models.CharField(max_length=40)
    door_num = models.IntegerField()
    transmission = models.CharField(
        max_length=10,
        choices = Transmission.choices,
        default=Transmission.AUTO
    )
    price = models.DecimalField(decimal_places=2, max_digits=999)

    def __str__(self):
        return f"{self.full_name}"