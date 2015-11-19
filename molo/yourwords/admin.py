import json

from molo.core.models import ArticlePage, LanguagePage
from molo.yourwords.models import (
    YourWordsCompetitionEntry, YourWordsCompetition)
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.template.defaultfilters import truncatechars


def convert_to_article(model_admin, request, entry):
    [entry] = entry
    english = LanguagePage.objects.get(code='en')
    article = ArticlePage(
        title=entry.story_name,
        body=json.dumps([{"type": "paragraph", "value": entry.story_text}]))
    english.add_child(instance=article)
    article.save_revision()


convert_to_article.short_description = "Convert competition entry to article"


class YourWordsCompetitionEntryAdmin(admin.ModelAdmin):
    list_display = ['story_name', 'truncate_text', 'user', 'hide_real_name',
                    'submission_date', 'is_read', 'is_shortlisted', 'is_winner']
    list_filter = ['competition__slug', 'is_read', 'is_shortlisted',
                   'is_winner']
    list_editable = ['is_read', 'is_shortlisted', 'is_winner']

    def truncate_text(self, obj, *args, **kwargs):
        return truncatechars(obj.story_text, 30)

    actions = [convert_to_article]


class YourWordsCompetitionAdmin(admin.ModelAdmin):
    list_display = ['entries', 'start_date', 'end_date', 'live']
    list_filter = ['title', 'start_date', 'end_date']
    search_fields = ['title', 'content', 'description']

    def entries(self, obj, *args, **kwargs):
        url = reverse('admin:yourwords_yourwordscompetitionentry_changelist')
        return '<a href="%s?competition__slug=%s">%s</a>' % (
            url, obj.slug, obj)

    entries.allow_tags = True
    entries.short_description = 'Title'


admin.site.register(YourWordsCompetitionEntry, YourWordsCompetitionEntryAdmin)
admin.site.register(YourWordsCompetition, YourWordsCompetitionAdmin)
