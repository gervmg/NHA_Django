# Generated by Django 3.2.18 on 2023-07-08 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_voetbalspeler_datum_invoer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voetbalspeler',
            name='datum_invoer',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
