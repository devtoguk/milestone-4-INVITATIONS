# Generated by Django 3.1.5 on 2021-02-24 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20210223_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customdetailline',
            name='font',
            field=models.CharField(choices=[("'Clicker Script', cursive", "'Clicker Script', cursive"), ("'Londrina Solid', cursive", "'Londrina Solid', cursive"), ("'Audiowide', cursive", "'Audiowide', cursive"), ("'Playball', cursive", "'Playball', cursive"), ("'Sedgwick Ave', cursive", "'Sedgwick Ave', cursive"), ("'Press Start 2P', cursive", "'Press Start 2P', cursive"), ("'Bangers', cursive", "'Bangers', cursive"), ("'Righteous', cursive", "'Righteous', cursive"), ("'Roboto Condensed', sans-serif", "'Roboto Condensed', sans-serif"), ("'Waiting for the Sunrise', cursive", "'Waiting for the Sunrise', cursive"), ("'Courgette', cursive", "'Courgette', cursive")], default="'Bangers', cursive", max_length=60),
        ),
        migrations.AlterField(
            model_name='customdetailline',
            name='name',
            field=models.CharField(max_length=11),
        ),
    ]