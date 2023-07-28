# Generated by Django 4.2.3 on 2023-07-28 18:03

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('organ_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.organ')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('info_url', models.TextField()),
                ('normal_reference', models.TextField()),
                ('unit_of_measure', models.TextField()),
                ('panel_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.panel')),
            ],
        ),
    ]
