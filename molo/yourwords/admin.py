import json

from molo.core.models import ArticlePage, LanguagePage
from molo.yourwords.models import (
    YourWordsCompetitionEntry, YourWordsCompetition)
from django.contrib import admin
from django.core.urlresolvers import reverse


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
    list_display = ['story_name', 'story_text', 'user',
                    'submission_date']
    list_filter = ['competition__slug']
    actions = [convert_to_article]


class YourWordsCompetitionAdmin(admin.ModelAdmin):
    list_display = ['entries', 'start_date', 'end_date', 'live']
    list_filter = ['title', 'start_date', 'end_date', 'description']
    search_fields = ['title', 'content', 'description']

    def entries(self, obj, *args, **kwargs):
        url = reverse('admin:yourwords_yourwordscompetitionentry_changelist')
        return '<a href="%s?competition__slug=%s">%s</a>' % (
            url, obj.slug, obj)
    entries.allow_tags = True
    entries.short_description = 'Title'


admin.site.register(YourWordsCompetitionEntry, YourWordsCompetitionEntryAdmin)
admin.site.register(YourWordsCompetition, YourWordsCompetitionAdmin)
