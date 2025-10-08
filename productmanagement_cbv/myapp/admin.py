from django.contrib import admin
from myapp.models import Product


@admin.register(Product)
class ProduactAdmin(admin.ModelAdmin):
    list_display = ['id','name','price']