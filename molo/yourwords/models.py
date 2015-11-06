from wagtail.wagtailcore.models import Page


class Competition(Page):
    description = Page.TextField()
    content = Page.TextField()
    start_date = Page.DateTimeField(null=True, blank=True)
    end_date = Page.DateTimeField(null=True, blank=True)


class CompetitionEntry(Page):
    story_name = Page.CharField(max_length=128)
    story_text = Page.TextField()
    terms_or_conditions_approved = Page.BooleanField()
    hide_real_name = Page.BooleanField()
