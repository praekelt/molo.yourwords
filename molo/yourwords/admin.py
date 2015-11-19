import json

from molo.core.models import ArticlePage, LanguagePage
from molo.yourwords.models import YourWordsCompetitionEntry, YourWordsCompetition
from django.contrib import admin


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
    list_display = ['competition', 'story_name', 'user', 'story_text']
    actions = [convert_to_article]


class YourWordsCompetitionAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'live']
    list_filter = ['title', 'start_date', 'end_date']
    search_fields = ['title', 'content', 'description']


admin.site.register(YourWordsCompetitionEntry, YourWordsCompetitionEntryAdmin)
admin.site.register(YourWordsCompetition, YourWordsCompetitionAdmin)
