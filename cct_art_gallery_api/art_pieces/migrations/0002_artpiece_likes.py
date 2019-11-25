# Generated by Django 2.2.7 on 2019-11-25 01:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('art_pieces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artpiece',
            name='likes',
            field=models.ManyToManyField(related_name='artpieces', to=settings.AUTH_USER_MODEL),
        ),
    ]
