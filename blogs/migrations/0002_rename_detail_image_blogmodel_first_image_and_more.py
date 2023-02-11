# Generated by Django 4.1.5 on 2023-02-10 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogmodel',
            old_name='detail_image',
            new_name='first_image',
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='second_image',
            field=models.ImageField(default=None, upload_to='blogs/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
