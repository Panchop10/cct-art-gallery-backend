# Generated by Django 2.2.7 on 2019-11-25 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art_pieces', '0003_artpiece_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtPieceTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('name', models.CharField(max_length=50, verbose_name='art piece tag')),
                ('art_piece', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tags', to='art_pieces.ArtPiece')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArtPieceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('name', models.CharField(max_length=100, verbose_name='art piece detail detail')),
                ('art_piece', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='details', to='art_pieces.ArtPiece')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]