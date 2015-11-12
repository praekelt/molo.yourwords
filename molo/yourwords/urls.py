from molo.yourwords import views

from django.conf.urls import patterns, url

# from django.contrib.auth.decorators import login_required

urlpatterns = patterns(
    '',
    url(
        r'^entry/(?P<competition_id>\d+)/$',
        views.CompetitionEntry.as_view(),
        name='competition_entry'),
    url(
        r'^thankyou/(?P<competition_id>\d+)/$',
        views.ThankYouView.as_view(),
        name='thank_you'),
)
