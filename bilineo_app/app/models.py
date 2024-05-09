from django.db import models

# Create your models here.
class Store(models.Model):
   store_name = models.CharField(max_length=100)

class FoodItem(models.Model):
   food_name = models.CharField(max_length=100)
   unit_price = models.PositiveIntegerField()
   store = models.ForeignKey(Store, on_delete=models.CASCADE)

class TrayItem(models.Model):
   store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
   food_id = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField(default=0)