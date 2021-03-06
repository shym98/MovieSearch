# Generated by Django 2.1 on 2018-08-22 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=50)),
                ('role_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField()),
                ('professions', models.CharField(max_length=100)),
                ('awards', models.ManyToManyField(to='moviesearch.Award')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release', models.DateField()),
                ('type', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=100)),
                ('length', models.DurationField()),
                ('age_rating', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('poster_link', models.URLField()),
                ('trailer_link', models.URLField()),
                ('budget', models.IntegerField(verbose_name='budget in $')),
                ('ww_gross', models.IntegerField(verbose_name='world wide gross')),
                ('awards', models.ManyToManyField(to='moviesearch.Award')),
            ],
        ),
        migrations.AddField(
            model_name='crew',
            name='human',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='moviesearch.Human'),
        ),
        migrations.AddField(
            model_name='crew',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviesearch.Movie'),
        ),
    ]
