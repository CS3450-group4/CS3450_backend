# Generated by Django 4.1.1 on 2022-10-30 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0011_remove_userinfo_password_remove_userinfo_username_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="actingLevel",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
