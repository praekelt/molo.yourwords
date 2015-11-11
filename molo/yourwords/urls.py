from molo.yourwords import views

from django.conf.urls import patterns, url
# from django.contrib.auth.decorators import login_required

urlpatterns = patterns(
    '',
    url(
        r'^entry/$',
        views.CompetitionEntry.as_view(
            template_name="yourwords/Your_words_competition.html"
        ),
        name='competition_entry'),
)
