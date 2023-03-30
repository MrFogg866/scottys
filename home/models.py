from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class SubscribedUsers(models.Model):
    email = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)


class Review(models.Model):
    RATING_CHOICES = (
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    )

    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False, related_name='reviews', default=1)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.email