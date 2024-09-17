from rest_framework import serializers
from django.core.exceptions import ValidationError as DjangoValidationError

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор модели Product."""
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')

    # def validate(self, value):
    #     """Дополнительная валидация цены на уровне сериализатора."""
    #     if value < 0:
    #         raise serializers.ValidationError(
    #             'Цена не может быть отрицательной!'
    #         )
    #     return value

