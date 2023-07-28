# Generated by Django 4.2.3 on 2023-07-28 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('organ_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.organ')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('info_url', models.CharField(max_length=100)),
                ('normal_reference', models.CharField(max_length=100)),
                ('unit_of_measure', models.CharField(max_length=100)),
                ('panel_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.panel')),
            ],
        ),
    ]
