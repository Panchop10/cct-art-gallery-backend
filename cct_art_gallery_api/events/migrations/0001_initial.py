# Generated by Django 2.2.7 on 2019-11-25 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('art_pieces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('name', models.CharField(max_length=150, verbose_name='event name')),
                ('date', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True, verbose_name='artist biography')),
                ('location', models.CharField(max_length=255, verbose_name='location of the event')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='events/pictures/', verbose_name='event banner')),
                ('finished', models.BooleanField(default=False, help_text='Tell us if a event is finished or not')),
                ('artpieces', models.ManyToManyField(related_name='events', to='art_pieces.ArtPiece')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
