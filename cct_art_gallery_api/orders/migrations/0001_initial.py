# Generated by Django 2.2.7 on 2019-11-25 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('total', models.PositiveIntegerField()),
                ('payment_method', models.CharField(max_length=150)),
                ('delivered', models.BooleanField(default=False, help_text='Tell us if a order was delivered or not')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
