# Generated by Django 3.2.4 on 2021-08-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_norm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='normalization',
            name='error_message',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='normalization',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
