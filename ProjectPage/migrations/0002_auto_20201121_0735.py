# Generated by Django 3.1.3 on 2020-11-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodels',
            name='description',
            field=models.CharField(max_length=800),
        ),
    ]
