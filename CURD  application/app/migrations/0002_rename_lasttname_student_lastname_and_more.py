# Generated by Django 5.0.2 on 2024-02-17 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Lasttname',
            new_name='Lastname',
        ),
        migrations.AlterField(
            model_name='student',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
    ]
