# Generated by Django 3.0.3 on 2020-03-02 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20200302_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slpaddress',
            name='address',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
