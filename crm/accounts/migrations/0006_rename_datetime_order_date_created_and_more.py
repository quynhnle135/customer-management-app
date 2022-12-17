# Generated by Django 4.1.4 on 2022-12-17 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_order_tag_product_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='datetime',
            new_name='date_created',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]