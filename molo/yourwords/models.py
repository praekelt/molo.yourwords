from wagtail.wagtailcore.models import Page


class Competition(Page):
    description = Page.TextField()
    content = Page.TextField()
    start_date = Page.DateTimeField(null=True, blank=True)
    end_date = Page.DateTimeField(null=True, blank=True)


class CompetitionEntry(Page):
    story_name = Page.CharField(max_length=128)
    story_text = Page.TextField()
    TERMS_OR_CONDITIONS_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    terms_or_conditions_approved = Page.BooleanField(
        choices=TERMS_OR_CONDITIONS_CHOICES)
    HIDE_REAL_NAME_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    hide_real_name = Page.BooleanField(choices=HIDE_REAL_NAME_CHOICES)
