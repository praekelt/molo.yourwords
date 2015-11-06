from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    MultiFieldPanel)


class Competition(Page):
    name = Page.CharField(max_length=128)
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


class wagtailCompetition(Page):
    description = Page.TextField(null=True, blank=True),
    content = Page.TextField(null=True, blank=True),
    startDate = Page.DateTimeField(null=True, blank=True)
    closingDate = Page.DateTimeField(null=True, blank=True)

    def articles(self):
        return wagtailCompetition.objects.live().child_of(self)

    def sections(self):
        return wagtailCompetition.objects.live().child_of(self)

    def get_effective_extra_style_hints(self):
        # The extra css is inherited from the parent SectionPage.
        # This will either return the current value or a value
        # from its parents.
        parent_section = wagtailCompetition.objects.all().ancestor_of(self).last()
        if parent_section:
            return self.extra_style_hints or \
                parent_section.get_effective_extra_style_hints()
        else:
            return self.extra_style_hints

    def get_parent_section(self):
        return wagtailCompetition.objects.all().ancestor_of(self).last()

    class Meta:
        verbose_name = _('Section')

wagtailCompetition.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('description'),
    MultiFieldPanel(
        [
            FieldPanel('startDate'),
            FieldPanel('closingDate'),
        ],
        heading="Publishing",)
]

wagtailCompetition.settings_panels = [
    MultiFieldPanel(
        Page.settings_panels, "Scheduled publishing", "publishing"),
    MultiFieldPanel(
        [FieldRowPanel(
            [FieldPanel('extra_style_hints')], classname="label-above")],
        "Meta")
]
