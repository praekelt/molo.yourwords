from molo.core.models import ArticlePage
from molo.yourwords.models import YourWordsCompetitionEntry
from molo.yourwords.admin import ConvertToArticle, ArticleAdmin
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User


class TestAdminActions(TestCase):
    fixtures = ['molo/yourwords/tests/fixtures/test.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='tester',
            email='tester@example.com',
            password='tester')

    def test_convert_to_article(self):
        entry = YourWordsCompetitionEntry.objects.create(
            story_name='test',
            story_text='test body',
            terms_or_conditions_approved=True,
            hide_real_name=True
        )
        request = self.factory.get('/home/english/')
        request.user = self.user
        ConvertToArticle(ArticleAdmin, request, entry)
        article = ArticlePage.objects.get(title='test')
        self.assertEquals(article.title, entry.story_name)
