# Generated by Django 3.2.2 on 2021-05-16 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designer', '0006_auto_20210516_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designs',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
