from django.db import models


class competition(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
