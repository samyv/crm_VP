# Generated by Django 3.1.4 on 2021-03-23 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0002_auto_20210323_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurance_contract',
            name='insurance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='controller.insurance'),
            preserve_default=False,
        ),
    ]
