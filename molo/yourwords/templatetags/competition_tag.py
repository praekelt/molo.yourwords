from django import template
from django.shortcuts import get_object_or_404
from wagtail.wagtailcore.models import Page
from copy import copy
from molo.yourwords.models import YourWordsCompetition

register = template.Library()


@register.inclusion_tag(
    'yourwords/your_words_competition.html',
    takes_context=True
)
def your_words_competition(context, page=None):
    context = copy(context)
    context.update({
        'competition': YourWordsCompetition.objects.live().child_of(page)
    })
    return context
