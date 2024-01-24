# Generated by Django 5.0.1 on 2024-01-24 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='author',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='authors.author'),
        ),
    ]