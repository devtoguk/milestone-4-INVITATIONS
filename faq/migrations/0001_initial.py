# Generated by Django 3.1.5 on 2021-01-28 20:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=254)),
                ('answer', models.TextField(blank=True)),
                ('display', models.IntegerField(blank=True, default=50, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]