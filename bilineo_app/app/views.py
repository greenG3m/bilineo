from django.shortcuts import render
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
   restaurant_detail = FoodItem.objects.all()
   context = {
      'restaurant_detail': restaurant_detail,
   }
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