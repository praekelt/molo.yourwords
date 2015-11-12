from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from molo.yourwords.forms import CompetitionEntryForm


class CompetitionEntry(CreateView):
    form_class = CompetitionEntryForm
    template_name = 'yourwords/your_words_competition.html'

    def get_success_url(self):
        return reverse('molo.yourwords:thank_you', args=[self.object.id])


class CompetitionEntryView(FormView):
    template_name = 'yourwords/thank_you.html'
    form_class = CompetitionEntryForm

    def form_valid(self, form):

        return super(CompetitionEntryView, self).form_valid(form)
