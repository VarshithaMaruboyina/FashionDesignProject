# Generated by Django 3.2.2 on 2021-05-16 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('designer', '0015_alter_designs_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designs',
            name='description',
        ),
        migrations.RemoveField(
            model_name='designs',
            name='price',
        ),
    ]