# Generated by Django 5.1.3 on 2024-11-21 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('discount', models.CharField(blank=True, max_length=100, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groceryapp.category')),
            ],
        ),
    ]
