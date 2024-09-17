from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор модели Product."""
    price = serializers.FloatField(
        min_value=0,
        error_messages={'min_value': 'Цена не может быть отрицательной!'}
    )

    class Meta:
        model = Product
        fields = ('name', 'description', 'price')
