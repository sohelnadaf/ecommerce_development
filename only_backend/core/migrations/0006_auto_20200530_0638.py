# Generated by Django 2.2.10 on 2020-05-30 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200530_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='media_root'),
        ),
    ]
