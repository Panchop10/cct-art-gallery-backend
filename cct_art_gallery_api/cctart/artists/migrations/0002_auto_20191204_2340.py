# Generated by Django 2.2.7 on 2019-12-04 23:40

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='slug_name',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['first_name', 'last_name']),
        ),
    ]