from django.contrib import admin
from .models import (Customer,
                     Product,
                     Order,
                     OrderItem,
                     ShippingAddress,
                     Service,
                     Tablet,
                     Carousel,
                     Watch)

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Service)
admin.site.register(Tablet)
admin.site.register(Watch)
admin.site.register(Carousel)