# Generated by Django 3.0.3 on 2020-02-24 08:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200224_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]