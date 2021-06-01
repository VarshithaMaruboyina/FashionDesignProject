# Generated by Django 3.2.2 on 2021-05-06 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='designs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gmail', models.EmailField(max_length=100)),
                ('design', models.ImageField(upload_to='images/')),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'designs',
            },
        ),
    ]