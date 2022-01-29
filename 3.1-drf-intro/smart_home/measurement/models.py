from django.db import models


class Sensor(models.Model):

    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.CharField(max_length=250, verbose_name='Описание')

    class Meta:
        ordering = ['id']


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, db_column='sensor', on_delete=models.CASCADE, related_name='measurements',
                               verbose_name='Показания')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата измерения')

    class Meta:
        ordering = ['created_at']
