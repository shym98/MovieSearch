from django.db import models


class Award(models.Model):
    name        = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    date        = models.DateField()


class Movie(models.Model):
    title           = models.CharField(max_length=100)
    release         = models.DateField()
    type            = models.CharField(max_length=10)
    genre           = models.CharField(max_length=100)
    length          = models.DurationField()
    age_rating      = models.CharField(max_length=10)
    description     = models.TextField()

    poster_link     = models.URLField()
    trailer_link    = models.URLField()

    budget          = models.IntegerField('budget in $')
    ww_gross        = models.IntegerField('world wide gross')
    awards          = models.ManyToManyField(Award, )

    # user_rating     = models.FloatField()
    # site_links      = models.CharField(max_length=200)

    def __str__(self):
        return '%s (%s)' % (self.title, self.release.year)


class Human(models.Model):
    first_name  = models.CharField(max_length=100)
    last_name   = models.CharField(max_length=100)
    biography   = models.TextField()
    birth_date  = models.DateField()
    death_date  = models.DateField()
    professions = models.CharField(max_length=100)
    awards      = models.ManyToManyField(Award)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Crew(models.Model):
    movie       = models.ForeignKey(Movie, on_delete=models.CASCADE)
    human       = models.ForeignKey(Human, on_delete=models.PROTECT)
    profession  = models.CharField(max_length=50)
    role_name   = models.CharField(max_length=100)