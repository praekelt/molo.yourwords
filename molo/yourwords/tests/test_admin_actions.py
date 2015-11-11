from molo.core.models import ArticlePage
from molo.yourwords.models import YourWordsCompetitionEntry
from molo.yourwords.admin import ConvertToArticle, ArticleAdmin
from django.test import TestCase


class TestAdminActions(TestCase):
    def test_convert_to_article(self):
        entry = YourWordsCompetitionEntry.objects.create(
            story_name='test',
            story_text='test body',
            terms_or_conditions_approved=True,
            hide_real_name=True
        )
        ConvertToArticle(ArticleAdmin, None, entry)
        article = ArticlePage.objects.get(title='test')
        self.assertEquals(article.title, entry.story_name)
