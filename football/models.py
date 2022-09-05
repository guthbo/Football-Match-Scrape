from django.db import models

# Create your models here.


class Chempionat(models.Model):
    match = models.CharField("Championat:", max_length=200)
    country = models.CharField("Country:", max_length=200)
    date = models.CharField("Date:", max_length=200)
    time = models.CharField("Time:", max_length=200)

    def __str__(self):
        return self.name

    class Meta:

        verbose_name = "Match"
        verbose_name_plural = "Matches"
