from django.conf.urls import url

from plugins.reporting import views

urlpatterns = [
    url(r'^$',
        views.index,
        name='reporting_index'),
    url(r'^press/$',
        views.press,
        name='reporting_press'),
    url(r'^by_month/$',
        views.report_journal_usage_by_month,
        name='reporting_journal_usage_by_month'),
    url(r'^articles/(?P<journal_id>\d+)/$',
        views.report_articles,
        name='reporting_articles'),
    url(r'^production/$',
        views.report_production,
        name='reporting_production'),
    url(r'^review/$',
        views.report_review,
        name='reporting_review'),
    url(r'^review/journal/(?P<journal_id>\d+)/$',
        views.report_review,
        name='reporting_review_journal'),
    url(r'^geo/$',
        views.report_geo,
        name='reporting_geo'),
    url(r'^geo/(?P<journal_id>\d+)/$',
        views.report_geo,
        name='report_geo_journal'),
    url(r'^citations/articles/$',
        views.report_citations,
        name='report_citations'),
    url(r'^citations/$',
        views.report_all_citations,
        name='report_all_citations'),
    url(r'^citations/journal/(?P<journal_id>\d+)/$',
        views.report_journal_citations,
        name='report_journal_citations'),
    url(r'^citations/journal/(?P<journal_id>\d+)/article/(?P<article_id>\d+)/$',
        views.report_article_citing_works,
        name='report_article_citing_works'),
]
