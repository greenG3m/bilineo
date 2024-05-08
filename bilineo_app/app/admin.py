from django.contrib import admin
from .models import Store, FoodItem, TrayItem

# Register your models here.
admin.site.register(Store)
admin.site.register(FoodItem)
admin.site.register(TrayItem)