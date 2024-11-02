from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'amount']
    search_fields = ['name', 'category', 'subcategory']
    list_filter = ['category', 'subcategory']

    