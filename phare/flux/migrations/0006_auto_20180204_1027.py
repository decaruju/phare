# Generated by Django 2.0.1 on 2018-02-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0005_auto_20180203_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='horodatage',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
