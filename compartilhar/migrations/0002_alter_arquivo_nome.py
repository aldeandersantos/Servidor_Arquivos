# Generated by Django 4.2.15 on 2024-08-20 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compartilhar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='nome',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
