# Generated by Django 3.2.19 on 2023-05-24 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_basket_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firma',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
