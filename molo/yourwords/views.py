from django.views.generic.edit import CreateView
from molo.yourwords.forms import CompetitionEntryForm


class CompetitionEntry(CreateView):
    form_class = CompetitionEntryForm
    template_name = 'yourwords/Your_words_competition.html'
