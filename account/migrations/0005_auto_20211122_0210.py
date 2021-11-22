# Generated by Django 3.2.9 on 2021-11-21 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0004_alter_profile_random_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='random_url',
            field=models.UUIDField(default='aad0d3da', verbose_name='آدرس اختصاصی'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]