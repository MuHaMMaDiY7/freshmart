# Generated by Django 4.1.5 on 2023-02-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='real_price',
            field=models.FloatField(default=0),
        ),
    ]