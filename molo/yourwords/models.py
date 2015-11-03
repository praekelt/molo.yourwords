from django.db import models


class competition(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    COMPETITION_STATUS_CHOICES = (
            ('UC', 'Upcoming'),
            ('CR', 'Currently Running'),
            ('CL', 'Closed'),
    )
    competition_status = models.CharField(
        max_length=2,
        choices=COMPETITION_STATUS_CHOICES,
        blank=True,
        null=True,
    )
