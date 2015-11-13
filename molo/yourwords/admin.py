from molo.core.models import ArticlePage, LanguagePage
from molo.yourwords.models import YourWordsCompetitionEntry
from django.contrib import admin


def ConvertToArticle(model_admin, request, entry):
    english, is_created = LanguagePage.objects.get_or_create(code='en')
    article = ArticlePage(title=entry.story_name, body=entry.story_text)
    article.save()
    article.save_revision(
        user=request.user,
        submitted_for_moderation=False,
    )
    english.add_child(instance=article)
    english.save()


ConvertToArticle.short_description = "Convert competition entry to article"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']
    actions = [ConvertToArticle]

admin.site.register(YourWordsCompetitionEntry, ArticleAdmin)
