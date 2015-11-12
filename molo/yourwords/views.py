from django.views.generic.edit import CreateView
from molo.yourwords.forms import CompetitionEntryForm
from django.views.generic.edit import FormView


class CompetitionEntry(CreateView):
    form_class = CompetitionEntryForm
    template_name = 'yourwords/your_words_competition.html'


class CompetitionEntryView(FormView):
    template_name = 'thank_you.html'
    form_class = CompetitionEntryForm
    success_url = '/thanks/'

    def form_valid(self, form):

        return super(CompetitionEntryView, self).form_valid(form)
