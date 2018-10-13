from django.db import models


class Award(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.CharField(max_length=100)
    category = models.TextField()
    type = models.TextField()


class Crew(models.Model):
    human = models.CharField(max_length=100)
    role_name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    length = models.DurationField()
    age_rating = models.CharField(max_length=10)
    description = models.TextField()
    imdb_rating = models.CharField(max_length=20)
    rotten_rating = models.CharField(max_length=20)
    meta_rating = models.CharField(max_length=20)

    poster_link = models.URLField()
    trailer_link = models.URLField()
    imdb_link = models.URLField()
    rotten_link = models.URLField()
    meta_link = models.URLField()

    budget = models.BigIntegerField('budget in $')
    ww_gross = models.BigIntegerField('world wide gross')
    awards = models.ManyToManyField(Award, )
    crew = models.ManyToManyField(Crew, )

    user_id = models.IntegerField()

    def __str__(self):
        return '%s (%s)' % (self.title, self.release)

class Films(models.Model):
    year = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

class Human(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField()
    birth_date = models.CharField(max_length=100)
    death_date = models.CharField(max_length=100)
    professions = models.CharField(max_length=100)
    awards = models.ManyToManyField(Award)
    highest_rating = models.CharField(max_length=100)
    lowest_rating = models.CharField(max_length=100)

    imdb_link = models.URLField()
    rotten_link = models.URLField()
    photo_link = models.URLField()

    user_id = models.IntegerField()

    films = models.ManyToManyField(Films)

    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return self.full_name()


class Request(models.Model):
    user_id = models.IntegerField()
    request = models.CharField(max_length=100)
