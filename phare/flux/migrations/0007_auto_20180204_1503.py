# Generated by Django 2.0.1 on 2018-02-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0006_auto_20180204_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='citoyen',
            name='matiere_dangereuse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='citoyen',
            name='mobilite_reduite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='citoyen',
            name='nombre_individus',
            field=models.IntegerField(default=1),
        ),
    ]
