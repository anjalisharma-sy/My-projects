# Generated by Django 4.2.2 on 2023-08-11 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0002_consume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='carbohydrates',
            new_name='carbs',
        ),
    ]