# Generated by Django 5.0.1 on 2024-01-27 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=100)),
                ('taskDescription', models.TextField()),
                ('is_Completed', models.BooleanField(default=False)),
                ('TaskAssignDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
