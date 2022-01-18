from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.TextField(max_length=255)
    image = models.EmailField(max_length=255)
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=255, unique=True)
