import json

from django.contrib import admin
from django.core.urlresolvers import reverse
from django.template.defaultfilters import truncatechars
from django import forms

from molo.core.models import ArticlePage, LanguagePage
from molo.yourwords.models import (
    YourWordsCompetitionEntry, YourWordsCompetition)


def convert_to_article(model_admin, request, entry):
    [entry] = entry
    english = LanguagePage.objects.get(code='en')
    article = ArticlePage(
        title=entry.story_name,
        body=json.dumps([{"type": "paragraph", "value": entry.story_text}]))
    english.add_child(instance=article)
    article.save_revision()


convert_to_article.short_description = "Convert competition entry to article"


class YourWordsCompetitionEntryForm(forms.ModelForm):

    class Meta:
        model = YourWordsCompetitionEntry
        fields = ['story_name', 'story_text', 'user', 'hide_real_name',
                  'is_read', 'is_shortlisted', 'is_winner']


class YourWordsCompetitionEntryAdmin(admin.ModelAdmin):
    list_display = ['story_name', 'truncate_text', 'user', 'hide_real_name',
                    'submission_date', 'is_read', 'is_shortlisted',
                    'is_winner']
    list_filter = ['competition__slug', 'is_read', 'is_shortlisted',
                   'is_winner', 'submission_date']
    list_editable = ['is_read', 'is_shortlisted', 'is_winner']
    date_hierarchy = 'submission_date'
    form = YourWordsCompetitionEntryForm
    readonly_fields = ('competition', 'story_name', 'story_text', 'user',
                       'hide_real_name', 'submission_date')

    def truncate_text(self, obj, *args, **kwargs):
        return truncatechars(obj.story_text, 30)

    actions = [convert_to_article]


class YourWordsCompetitionAdmin(admin.ModelAdmin):
    list_display = ['entries', 'start_date', 'end_date', 'status',
                    'number_of_entries']
    list_filter = ['title', 'start_date', 'end_date']
    search_fields = ['title', 'content', 'description']
    date_hierarchy = 'start_date'

    def number_of_entries(self, obj, *args, **kwargs):
        return YourWordsCompetitionEntry.objects.filter(
            competition__slug=obj.slug).count()

    def status(self, obj, *args, **kwargs):
        if obj.live:
            return 'First published on ' + str(obj.first_published_at)
        return 'Unpublished'

    def entries(self, obj, *args, **kwargs):
        url = reverse('admin:yourwords_yourwordscompetitionentry_changelist')
        return '<a href="%s?competition__slug=%s">%s</a>' % (
            url, obj.slug, obj)

    entries.allow_tags = True
    entries.short_description = 'Title'


admin.site.register(YourWordsCompetitionEntry, YourWordsCompetitionEntryAdmin)
admin.site.register(YourWordsCompetition, YourWordsCompetitionAdmin)
