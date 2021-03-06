# Generated by Django 3.0.3 on 2020-03-20 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20200318_0825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sendto',
            options={'verbose_name': 'Send To', 'verbose_name_plural': 'Send To'},
        ),
        migrations.AddField(
            model_name='subscription',
            name='slp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='main.SlpAddress'),
        ),
        migrations.AlterField(
            model_name='slpaddress',
            name='transactions',
            field=models.ManyToManyField(related_name='slpaddress', to='main.Transaction'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='subscription',
            field=models.ManyToManyField(related_name='subscriber', to='main.Subscription'),
        ),
    ]
