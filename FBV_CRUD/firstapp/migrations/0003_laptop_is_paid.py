# Generated by Django 3.2.9 on 2021-11-22 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20211122_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
