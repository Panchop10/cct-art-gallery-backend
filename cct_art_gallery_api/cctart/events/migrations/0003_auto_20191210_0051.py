# Generated by Django 2.2.7 on 2019-12-10 00:51

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20191209_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug_name',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name'),
        ),
    ]