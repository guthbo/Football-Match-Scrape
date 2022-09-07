from django.db import models

# Create your models here.


class Championat(models.Model):
    match = models.CharField("Championat:", max_length=200)
    country = models.CharField("Country:", max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.match, self.country

    class Meta:

        verbose_name = "Championat"
        verbose_name_plural = "Championats"


class Team(models.Model):
    team = models.CharField("Team:", max_length=30)
    logo = models.ImageField(upload_to="uploads/")
    is_guest = models.BooleanField()

    def __str__(self):
        return self.team

    class Meta:
        verbose_name = "Team"


class Matches(models.Model):
    date = models.CharField("Date: ", max_length=30)
    score = models.CharField("Score: ", max_length=30)
    # is_guest = models.BooleanField()
    team_one = models.CharField("Team 1: ", max_length=30)
    team_two = models.CharField("Team 2: ", max_length=30)

    def __str__(self):
        return self.team_one + " vs " + self.team_two

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"
