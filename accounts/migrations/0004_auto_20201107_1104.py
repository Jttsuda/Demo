# Generated by Django 3.1.2 on 2020-11-07 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201107_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listitem',
            name='product',
        ),
        migrations.AddField(
            model_name='listitem',
            name='product_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='listitem',
            name='product_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='listitem',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]