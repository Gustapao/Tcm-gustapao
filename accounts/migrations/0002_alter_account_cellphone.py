# Generated by Django 4.1 on 2022-09-09 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="cellphone",
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]