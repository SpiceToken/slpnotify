# Generated by Django 3.0.3 on 2020-03-20 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20200320_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='main.SendTo'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='token',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to='main.Token'),
        ),
    ]
