import datetime

from molo.core.models import SiteLanguage, ArticlePage
from molo.core.tests.base import MoloTestCaseMixin

from molo.yourwords.models import (YourWordsCompetition,
                                   YourWordsCompetitionEntry,
                                   YourWordsCompetitionIndexPage)
from molo.yourwords.admin import (
    download_as_csv, YourWordsCompetitionEntryAdmin)

from django.test import TestCase, RequestFactory
from django.test.client import Client


class TestAdminActions(TestCase, MoloTestCaseMixin):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = self.login()
        self.mk_main()
        # Creates Main language
        self.english = SiteLanguage.objects.create(locale='en')
        # Create competition index page
        self.competition_index = YourWordsCompetitionIndexPage(
            title='Your words competition', slug='Your-words-competition')
        self.main.add_child(instance=self.competition_index)
        self.competition_index.save_revision().publish()

    def test_download_as_csv(self):
        comp = YourWordsCompetition(
            title='Test Competition',
            description='This is the description')
        self.competition_index.add_child(instance=comp)
        comp.save_revision().publish()

        YourWordsCompetitionEntry.objects.create(
            competition=comp,
            user=self.user,
            story_name='test',
            story_text='test body',
            terms_or_conditions_approved=True,
            hide_real_name=True
        )
        client = Client()
        client.login(username='superuser', password='pass')
        response = download_as_csv(YourWordsCompetitionEntryAdmin,
                                   None,
                                   YourWordsCompetitionEntry.objects.all())
        date = str(datetime.datetime.now().date())
        expected_output = ('Content-Type: text/csv\r\nContent-Disposition:'
                           ' attachment;filename=export.csv\r\n\r\nid,'
                           'competition,submission_date,user,story_name,'
                           'story_text,terms_or_conditions_approved,'
                           'hide_real_name,is_read,is_shortlisted,'
                           'is_winner,article_page\r\n1,Test Competition,' +
                           date + ',superuser,test,test body,'
                           'True,True,False,False,False,\r\n')
        self.assertEquals(str(response), expected_output)

    def test_convert_to_article(self):
        comp = YourWordsCompetition(
            title='Test Competition',
            description='This is the description')
        self.competition_index.add_child(instance=comp)
        comp.save_revision().publish()

        entry = YourWordsCompetitionEntry.objects.create(
            competition=comp,
            user=self.user,
            story_name='test',
            story_text='test body',
            terms_or_conditions_approved=True,
            hide_real_name=True
        )
        client = Client()
        client.login(username='superuser', password='pass')
        response = client.get(
            '/django-admin/yourwords/yourwordscompetitionentry/%d/convert/' %
            entry.id)
        article = ArticlePage.objects.get(title='test')
        entry = YourWordsCompetitionEntry.objects.get(pk=entry.pk)
        self.assertEquals(entry.story_name, article.title)
        self.assertEquals(entry.article_page, article)
        self.assertEquals(article.body.stream_data, [{
            "type": "paragraph", "value": "Written by: Anonymous",
            "type": "paragraph", "value": entry.story_text,
        }])

        self.assertEquals(ArticlePage.objects.all().count(), 1)
        self.assertEquals(
            response['Location'],
            '/admin/pages/%d/move/' % article.id)

        # second time it should redirect to the edit page
        response = client.get(
            '/django-admin/yourwords/yourwordscompetitionentry/%d/convert/' %
            entry.id)
        self.assertEquals(
            response['Location'],
            '/admin/pages/%d/edit/' % article.id)
        self.assertEquals(ArticlePage.objects.all().count(), 1)
