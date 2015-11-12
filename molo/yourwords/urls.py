from molo.yourwords import views

from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
# from django.contrib.auth.decorators import login_required

urlpatterns = patterns(
    '',
    url(
        r'^entry/$',
        views.CompetitionEntry.as_view(),
        name='competition_entry'),
    url(
        r'^entry/thankyou/(?P<competition_entry_id>\d+)/$',
        TemplateView.as_view(template_name='yourwords/thank_you.html'),
        name='thank_you'),
)
