# Generated by Django 4.2.20 on 2025-04-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_place_options_alter_placeimage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeimage',
            name='position',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Позиция'),
        ),
    ]
