# Generated by Django 3.2.9 on 2021-11-21 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_random_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='random_url',
            field=models.UUIDField(default='1C1E1EA4', verbose_name='آدرس اختصاصی'),
        ),
    ]