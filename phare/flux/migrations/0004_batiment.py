# Generated by Django 2.0.1 on 2018-02-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0003_citoyen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.CharField(max_length=30)),
                ('code_postal', models.CharField(max_length=6)),
                ('population', models.IntegerField(default=-1)),
                ('mobilite_reduite', models.BooleanField()),
                ('type_batiment', models.CharField(choices=[('r', 'résidentiel'), ('c', 'commercial'), ('b', 'bureau'), ('i', 'industriel'), ('p', 'public')], max_length=1)),
                ('gaz_naturel', models.BooleanField()),
                ('propane', models.BooleanField()),
                ('autre_danger', models.CharField(max_length=80)),
            ],
        ),
    ]