from rest_framework import serializers

from .models import Customer, Order, Email, CustomProduct


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = (
            'email',
        )


class UserSerializer(serializers.ModelSerializer):
    email = EmailSerializer()

    class Meta:
        model = Customer
        fields = (
            'email', 'first_name', 'last_name'
        )


class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer()

    class Meta:
        model = Order
        fields = (
            'customer', 'order_number'
        )


class CustomProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomProduct
        fields = (
            'name', 'price'
        )


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()

    class Meta:
        model = Order
        fields = (
            'order',
        )

