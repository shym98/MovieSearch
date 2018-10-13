from django.db import models
from django.contrib.auth.models import User
from index.models import Movie, Human

class MovieRequest(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    ready       = models.BooleanField(default=False)

    title       = models.TextField()
    year_from   = models.IntegerField(null=True)
    year_to     = models.IntegerField(null=True)
    genre       = models.TextField()

    def is_valid(self):
        errors = []

        if self.year_from and self.year_to:
            if self.year_from > self.year_to:
                errors.append("Year to should be later then year from")

        if len(self.title) == 0:
            if not self.year_to or not self.year_from:
                errors.append("You should enter year diapason")

        return errors


class MovieRequestResult(models.Model):
    request     = models.ForeignKey(MovieRequest, on_delete=models.CASCADE)
    movie       = models.ForeignKey(Movie, on_delete=models.CASCADE)

class HumanRequest(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    ready               = models.BooleanField(default=False)
    name                = models.TextField()
    living_year_from    = models.IntegerField(null=True)
    living_year_to      = models.IntegerField(null=True)
    profession          = models.TextField()
    def is_valid(self):
        errors = []
        if self.living_year_from and self.living_year_to:
            if self.living_year_from > self.living_year_to:
                errors.append("Year to should be later then year from")
        if len(self.name) == 0:
            if not self.living_year_to or not self.living_year_from:
                errors.append("You should enter year diapason")
        return errors

class HumanRequestResult(models.Model):
    request     = models.ForeignKey(HumanRequest, on_delete=models.CASCADE)
    human       = models.ForeignKey(Human, on_delete=models.CASCADE)

class MovieSubscription(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    movie   = models.ForeignKey(Movie, on_delete=models.CASCADE)