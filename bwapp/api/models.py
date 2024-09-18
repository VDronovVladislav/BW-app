from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """Модель продукта."""
    name = models.CharField(max_length=56, null=False)
    description = models.TextField()
    price = models.FloatField(
        validators=[
            MinValueValidator(
                limit_value=0,
                message='Цена не может быть отрицательной!'
            ),
        ]
    )

    def __str__(self):
        return self.name
