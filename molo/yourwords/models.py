from wagtail.wagtailcore.models import Page


class competition(Page):
    name = Page.CharField(max_length=128)
    startDate = Page.DateTimeField(null=True, blank=True)
    endDate = Page.DateTimeField(null=True, blank=True)
