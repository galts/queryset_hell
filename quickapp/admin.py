from django.contrib import admin

from .models import Email, Customer, Status, Order, CustomProduct, NonCustomProduct, OrderItem


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomProduct)
class CustomProductAdmin(admin.ModelAdmin):
    pass


@admin.register(NonCustomProduct)
class NonCustomProductAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
