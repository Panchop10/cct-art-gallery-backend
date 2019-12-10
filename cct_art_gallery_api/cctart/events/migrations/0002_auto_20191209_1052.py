# Generated by Django 2.2.7 on 2019-12-09 10:52

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='deleted',
            field=models.BooleanField(default=False, help_text='Tell us if a event was deleted or not'),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug_name',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['name', 'date']),
        ),
    ]