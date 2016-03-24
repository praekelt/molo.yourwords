from django import template
from copy import copy
from molo.yourwords.models import YourWordsCompetition

register = template.Library()


@register.inclusion_tag(
    'yourwords/your_words_competition_tag.html',
    takes_context=True
)
def your_words_competition(context, page=None):
    context = copy(context)

    if page:
        competition = YourWordsCompetition.objects.live().child_of(page)
    else:
        competition = None

    context.update({
        'competitions': competition
    })
    return context
