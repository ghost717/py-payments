# Generated by Django 2.1.5 on 2019-03-02 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_treningi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='cat',
            field=models.IntegerField(choices=[(2, 'Wpływ'), (1, 'Płatność stała'), (0, 'Płatność')], default=0),
        ),
        migrations.AlterField(
            model_name='treningi',
            name='ex01',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treningi',
            name='ex02',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treningi',
            name='ex03',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treningi',
            name='ex04',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treningi',
            name='ex05',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treningi',
            name='ex06',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treningi',
            name='ex07',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treningi',
            name='ex08',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treningi',
            name='ex09',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='treningi',
            name='ex10',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
