# Generated by Django 3.2.2 on 2021-05-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designer', '0016_auto_20210516_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='designs',
            name='description',
            field=models.CharField(default='NULL', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='designs',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]