# Generated by Django 3.2 on 2022-02-11 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisements', '0002_alter_advertisement_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertisement', models.ForeignKey(db_column='advertisement', on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to='advertisements.advertisement')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='advertisements', through='advertisements.Favourites', to=settings.AUTH_USER_MODEL),
        ),
    ]