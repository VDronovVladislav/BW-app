from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор модели Product."""
    name = serializers.CharField(
        allow_blank=False,
        error_messages={'blank': 'Название товара не может быть пустым!'}
    )
    price = serializers.FloatField(
        min_value=0,
        error_messages={'min_value': 'Цена не может быть отрицательной!'}
    )

    class Meta:
        model = Product
        fields = ('name', 'description', 'price')
