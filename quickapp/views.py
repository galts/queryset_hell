from django.db.models import Case, Exists, OuterRef, When, BooleanField
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import OrderItem, CustomProduct
from .serializers import OrderItemSerializer


class TestView(ListAPIView):
    # queryset = Order.objects.select_related('customer')\
    #     .select_related('customer__email')\
    #     .filter(status__paid=True)\
    # print(queryset.query)
    queryset = OrderItem.objects\
        .select_related('order')\
        .select_related('order__customer')\
        .select_related('order__customer__email')\
        .select_related('custom_product') \
        .select_related('non_custom_product') \
        .filter(order__status__paid=True)\
        .annotate(
            cp_exists=Case(
                When(
                    Exists(CustomProduct.objects.filter(custom_product=OuterRef('id'))),
                    then=True,
                ),
                default=False,
                output_field=BooleanField(),
            ),
        )
    serializer_class = OrderItemSerializer
    permission_classes = (AllowAny,)



