from django import forms

from molo.yourwords.models import YourWordsCompetitionEntry


class CompetitionEntryForm(forms.ModelForm):
    class Meta:
        model = YourWordsCompetitionEntry
        fields = ['story_name', 'story_text', 'terms_or_conditions_approved',
                  'hide_real_name']
