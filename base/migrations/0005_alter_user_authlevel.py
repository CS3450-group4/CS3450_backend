# Generated by Django 4.1.1 on 2022-10-09 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_menuitem_size_order_ingredients_list_delete_drink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='authLevel',
            field=models.JSONField(default=dict),
        ),
    ]
