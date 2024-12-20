# Generated by Django 5.0.1 on 2024-04-05 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('email', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
