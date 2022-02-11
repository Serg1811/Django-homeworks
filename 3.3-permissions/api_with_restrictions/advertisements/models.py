from django.conf import settings
from django.db import models


class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""

    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"
    DRAFT = "DRAFT", "Черновик"


class Advertisement(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    status = models.TextField(
        choices=AdvertisementStatusChoices.choices,
        default=AdvertisementStatusChoices.DRAFT
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='advertisements',
                                   through='Favourites',)


class Favourites(models.Model):
    advertisement = models.ForeignKey(
        Advertisement,
        db_column='advertisement',
        on_delete=models.CASCADE,
        related_name='favourites',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        db_column='user',
        on_delete=models.CASCADE,
        related_name='favourites',
    )
