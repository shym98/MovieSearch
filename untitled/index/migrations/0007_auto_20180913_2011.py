# Generated by Django 2.1 on 2018-09-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20180912_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='category',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='award',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='award',
            name='type',
            field=models.TextField(),
        ),
    ]
