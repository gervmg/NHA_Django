# Generated by Django 3.2.18 on 2023-07-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230705_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='voetbalspeler',
            name='aangepast',
            field=models.BooleanField(default=False),
        ),
    ]
