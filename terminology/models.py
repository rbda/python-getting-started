from django.db import models


class Term(models.Model):
    title = models.CharField(max_length=250)
    definition = models.CharField(max_length=250, blank=True)
    example = models.TextField(blank=True)
    url = models.URLField(max_length=250, blank=True)

    def __str__(self):
        return self.title
