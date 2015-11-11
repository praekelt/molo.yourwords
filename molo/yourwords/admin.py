from molo.core.models import ArticlePage
from molo.yourwords.models import YourWordsCompetitionEntry
from django.contrib import admin


def ConvertToArticle(model_admin, request, entry):
    root = request.site.root_page
    article = ArticlePage(title=entry.story_name, body=entry.story_text)
    root.add_child(instance=article)
ConvertToArticle.short_description = "Convert competition entry to article"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']
    actions = [ConvertToArticle]

admin.site.register(YourWordsCompetitionEntry, ArticleAdmin)
