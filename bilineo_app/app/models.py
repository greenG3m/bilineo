from django.db import models

# Create your models here.
class TRAY_ITEM(models.Model):
   store_name = models.CharField(max_length=100)
   food_name = models.CharField(max_length=100)
   unit_price = models.DecimalField(max_digits=5, decimal_places=2)
   quantity = models.PositiveIntegerField(default=1)

   # def __str__(self):
      # return f"{self.food_name} at {self.store_name} (${self.unit_price})"