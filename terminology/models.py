from django.db import models


class Term(models.Model):
    title = models.CharField(max_length=50)
    definition = models.CharField(max_length=50)
    example = models.TextField()
    url = models.URLField(max_length=250)

    def __str__(self):
        return self.title
