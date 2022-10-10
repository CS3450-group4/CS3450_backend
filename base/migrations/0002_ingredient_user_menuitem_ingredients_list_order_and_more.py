# Generated by Django 4.1.1 on 2022-10-04 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
                ('retailCost', models.PositiveIntegerField()),
                ('wholeSaleCost', models.PositiveIntegerField()),
                ('isMilk', models.BooleanField()),
                ('options', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authLevel', models.PositiveSmallIntegerField()),
                ('password', models.CharField(max_length=255)),
                ('userName', models.CharField(max_length=255)),
                ('balance', models.IntegerField()),
                ('actingLevel', models.PositiveSmallIntegerField()),
                ('hoursWorked', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='menuitem',
            name='ingredients_list',
            field=models.JSONField(default={}),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('orderStatus', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.user')),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('size', models.PositiveIntegerField()),
                ('additional_ingredients_list', models.JSONField(default={})),
                ('base_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.menuitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.order')),
            ],
        ),
    ]