from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin): ##sirve para personalizar

    list_display=("name","short_description","quantity")
    search_fields=("name", "short_description")
    list_filter=("name","fecha","quantity")
    date_hierarchy = "fecha"

admin.site.register(Product, ProductAdmin)
