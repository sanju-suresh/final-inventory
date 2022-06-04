# Generated by Django 4.0.4 on 2022-06-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0004_alter_item_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]