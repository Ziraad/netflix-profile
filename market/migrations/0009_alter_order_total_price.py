# Generated by Django 3.2.9 on 2021-11-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_alter_order_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='جمع کل'),
        ),
    ]