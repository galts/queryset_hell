from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


def _get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Email(models.Model):
    email = models.EmailField('email address')


class Customer(models.Model):
    first_name = models.CharField('first name', max_length=150)
    last_name = models.CharField('last name', max_length=150)
    email = models.ForeignKey(
        Email,
        on_delete=models.SET_NULL,
        verbose_name="email",
        null=True,
    )


class Status(models.Model):
    paid = models.BooleanField('paid status', default=False,)


class Order(models.Model):
    order_number = models.CharField(
        'order number', unique=True, max_length=256, db_index=True
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET(_get_sentinel_user),
        related_name='order_customer',
        verbose_name="customer",
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        verbose_name="status",
        null=True,
    )

    created_at = models.DateTimeField(
        'created at', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'updated at', auto_now=True
    )


class CustomProduct(models.Model):
    name = models.CharField('name', max_length=256)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(10000)]
    )


class NonCustomProduct(models.Model):
    name = models.CharField('name', max_length=256)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(10000)]
    )


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="order",
    )
    custom_product = models.ForeignKey(
        CustomProduct,
        on_delete=models.CASCADE,
        related_name='custom_product',
        verbose_name="custom_product",
    )
    non_custom_product = models.ForeignKey(
        NonCustomProduct,
        on_delete=models.CASCADE,
        verbose_name="non_custom_product",
    )

