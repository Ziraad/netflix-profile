from django.contrib import admin

from market.models import Order, Customer, Product

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
