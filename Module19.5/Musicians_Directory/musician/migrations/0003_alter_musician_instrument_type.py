# Generated by Django 5.0.1 on 2024-01-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0002_alter_musician_instrument_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='instrument_type',
            field=models.CharField(choices=[('Guitar', 'Guitar'), ('Piano', 'Piano'), ('Violin', 'Violin'), ('Drums', 'Drums'), ('Saxophone', 'Saxophone'), ('Other', 'Other')], max_length=20),
        ),
    ]