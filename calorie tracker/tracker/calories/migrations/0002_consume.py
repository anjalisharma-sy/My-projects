# Generated by Django 4.2.2 on 2023-08-07 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_consumed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calories.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
