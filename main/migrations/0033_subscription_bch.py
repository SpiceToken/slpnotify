# Generated by Django 3.0.3 on 2020-05-22 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20200521_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='bch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='main.BchAddress'),
        ),
    ]
