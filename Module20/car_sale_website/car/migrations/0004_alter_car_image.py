# Generated by Django 5.0.1 on 2024-02-07 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_brand_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/media/uploads/'),
        ),
    ]
