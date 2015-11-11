from molo.core.models import ArticlePage
from molo.yourwords.models import YourWordsCompetitionEntry
from django.contrib import admin


def ConvertToArticle(model_admin, request, entry):
    article = ArticlePage.objects.create(null, null)
    article.title = entry.story_name
    article.body = entry.story_text
ConvertToArticle.short_description = "Convert competition entry to article"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']
    actions = [ConvertToArticle]

admin.site.register(YourWordsCompetitionEntry, ArticleAdmin)
