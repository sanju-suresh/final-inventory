# Generated by Django 4.0.4 on 2022-06-01 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0002_rename_user_customer_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
