# Generated by Django 2.1.5 on 2019-02-24 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190223_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='cat',
            field=models.IntegerField(choices=[(1, 'Płatność stała'), (0, 'Płatność'), (2, 'Wpływ')], default=0),
        ),
    ]