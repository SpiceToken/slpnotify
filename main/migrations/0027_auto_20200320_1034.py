# Generated by Django 3.0.3 on 2020-03-20 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20200320_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slpaddress',
            name='transactions',
            field=models.ManyToManyField(blank=True, related_name='slpaddress', to='main.Transaction'),
        ),
    ]
