# Generated by Django 4.0.4 on 2022-06-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0005_issue_returned_alter_item_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='numberofitems',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
