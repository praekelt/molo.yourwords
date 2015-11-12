from django.shortcuts import get_object_or_404

from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse

from molo.yourwords.forms import CompetitionEntryForm
from molo.yourwords.models import YourWordsCompetition


class CompetitionEntry(CreateView):
    form_class = CompetitionEntryForm
    template_name = 'yourwords/your_words_competition.html'

    def get_context_data(self, *args, **kwargs):
        context = super(
            CompetitionEntry, self).get_context_data(*args, **kwargs)
        return context

    def get_success_url(self):
        return reverse(
            'molo.yourwords:thank_you',
            args=[self.object.competition.id])


class CompetitionEntryView(FormView):
    template_name = 'yourwords/thank_you.html'
    form_class = CompetitionEntryForm

    def form_valid(self, form):

        return super(CompetitionEntryView, self).form_valid(form)


class ThankYouView(TemplateView):
    template_name = 'yourwords/thank_you.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ThankYouView, self).get_context_data(*args, **kwargs)
        competition = get_object_or_404(
            YourWordsCompetition, id=kwargs.get('competition_id'))
        context.update({'competition': competition})
        return context
