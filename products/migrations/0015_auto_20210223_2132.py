# Generated by Django 3.1.5 on 2021-02-23 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20210223_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customdetailline',
            name='font',
            field=models.CharField(choices=[("'Clicker Script', cursive", "'Clicker Script', cursive"), ("'Londrina Solid', cursive", "'Londrina Solid', cursive"), ("'Audiowide', cursive", "'Audiowide', cursive"), ("'Playball', cursive", "'Playball', cursive"), ("'Sedgwick Ave', cursive", "'Sedgwick Ave', cursive"), ("'Press Start 2P', cursive", "'Press Start 2P', cursive"), ("'Bangers', cursive", "'Bangers', cursive"), ("'Righteous', cursive", "'Righteous', cursive"), ("'Roboto Condensed', sans-serif", "'Roboto Condensed', sans-serif")], default="'Clicker Script', cursive", max_length=60),
        ),
    ]
