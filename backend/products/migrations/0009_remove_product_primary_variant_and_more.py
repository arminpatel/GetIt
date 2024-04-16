# Generated by Django 4.2 on 2024-03-23 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_product_primary_variant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='primary_variant',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product_variation_id',
        ),
        migrations.RemoveField(
            model_name='productvariation',
            name='Product',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='products.product'),
        ),
    ]
