# Generated by Django 2.1 on 2018-09-12 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20180912_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.BigIntegerField(verbose_name='budget in $'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='ww_gross',
            field=models.BigIntegerField(verbose_name='world wide gross'),
        ),
    ]
