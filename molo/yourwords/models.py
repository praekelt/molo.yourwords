from wagtail.wagtailcore.models import Page
from django.db import models

from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock

from molo.core.blocks import MarkDownBlock


class Competition(Page):
    description = models.TextField(null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', MarkDownBlock()),
        ('image', ImageChooserBlock()),
        ('list', blocks.ListBlock(blocks.CharBlock(label="Item"))),
        ('numbered_list', blocks.ListBlock(blocks.CharBlock(label="Item"))),
        ('page', blocks.PageChooserBlock()),
    ], null=True, blank=True)

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    terms_and_conditions_link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=('Link to terms and conditions page')
    )


class CompetitionEntry(Page):
    story_name = models.CharField(max_length=128)
    story_text = models.TextField()
    terms_or_conditions_approved = models.BooleanField()
    hide_real_name = models.BooleanField()
