# Generated by Django 3.1.4 on 2021-03-23 18:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='created_on',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='birthdate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='created_on',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='phonenumber',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dog',
            name='sex',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('X', 'Other')], max_length=500),
        ),
        migrations.AlterField(
            model_name='member',
            name='sex',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('X', 'Other')], max_length=500),
        ),
        migrations.CreateModel(
            name='Insurance_contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_number', models.CharField(max_length=50)),
                ('expiry_date', models.DateField()),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controller.member')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_name', models.CharField(max_length=100)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='controller.address')),
            ],
        ),
    ]
