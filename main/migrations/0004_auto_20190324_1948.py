# Generated by Django 2.1.5 on 2019-03-24 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190302_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='valueType',
            field=models.IntegerField(blank=-1, null=True),
        ),
        migrations.AlterField(
            model_name='cat',
            name='cat',
            field=models.IntegerField(choices=[(0, 'Płatność'), (2, 'Wpływ'), (1, 'Płatność stała')], default=0),
        ),
    ]
