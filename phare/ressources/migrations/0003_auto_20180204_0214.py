# Generated by Django 2.0.1 on 2018-02-04 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ressources', '0002_auto_20180204_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ressource',
            old_name='a_biens_enssentiels',
            new_name='a_biens_essentiels',
        ),
    ]
