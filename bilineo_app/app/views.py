from django.shortcuts import render, get_object_or_404
from .models import Store, FoodItem, TrayItem
from .templates import *

# Create your views here.
def login_page(request):
   return render(request, "login_page.html")

def home_desktop(request):
   return render(request, "home_desktop.html")

def messages_page(request):
   return render(request, "messages_page.html")

def orders_page(request):
   return render(request, "orders_page.html")

def profile_page(request):
   return render(request, "profile_page.html")

def restaurant_detail_page(request):
   store_detail = FoodItem.objects.all()
   context = {
      'store_detail': store_detail,
   }
   return render(request, "restaurant_detail_page.html", context)

def add_food(request, store_id, food_id):
   store_detail = FoodItem.objects.all()
   context = {
      'store_detail': store_detail,
   }

   if request.method == 'POST':
      store = Store.objects.get(id=store_id)
      food = FoodItem.objects.get(id=food_id)
      new_tray_item = TrayItem.objects.create(food_id_id=food, store_id_id=store, quantity=1)
      new_tray_item.save()

   return render(request, "restaurant_detail_page.html", context)

def store_page(request):
   stores = Store.objects.all()
   context = {
      'stores': stores,
   }
   return render(request, "store_page.html", context)

def tray_page(request):
   stores = Store.objects.all()
   items = TrayItem.objects.all()
   context = {
      'stores': stores,
      'items': items,
   }
   return render(request, "tray_page.html", context)

def delete_tray_item(request, item_id): # Requests to delete an item
   item = get_object_or_404(TrayItem, id=item_id)
   stores = Store.objects.all()
   items = TrayItem.objects.all()
   context = {
      'stores': stores,
      'items': items,
   }

   if request.method == 'DELETE':
      item.delete()

   return render(request, "tray_page.html", context)