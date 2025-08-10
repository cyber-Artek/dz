from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.IntegerField(default=0)  # рейтинг (1–5)

    def __str__(self):
        return self.name
