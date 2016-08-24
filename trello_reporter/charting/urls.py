"""trello_reporter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    # TODO: sanitize URLs, do better namespacing
    # FIXME: API, HTML
    url(r'^$', views.index, name='index'),
    url(r'^board/(?P<board_id>[0-9]+)/$', views.board_detail, name='board-detail'),
    url(r'^board/(?P<board_id>[0-9]+)/refresh/$', views.board_refresh, name='board-refresh'),

    url(r'^list/(?P<list_id>[0-9]+)/$',
        views.list_detail, name='list-detail'),
    url(r'^card/(?P<card_id>[0-9]+)/$',
        views.card_detail, name='card-detail'),
    url(r'^sprint/(?P<sprint_id>[0-9]+)/$',
        views.sprint_detail, name='sprint-detail'),

    url(r'^chart/(?P<board_id>[0-9]+)/cards_at/$', views.cards_on_board_at, name='cards-at'),
    url(r'^chart/(?P<board_id>[0-9]+)/card_history/$', views.card_history, name='card-history'),

    url(r'^chart/(?P<board_id>[0-9]+)/$', views.show_cumulative_chart, name='show-cumulative-chart'),
    url(r'^chart/(?P<board_id>[0-9]+)/cumulative/$', views.cumulative_chart,
        name='cumulative-chart-data'),

    url(r'^chart/(?P<board_id>[0-9]+)/control/$', views.show_control_chart,
        name='show-control-chart'),
    url(r'^chart/(?P<board_id>[0-9]+)/control-data/$', views.control_chart,
        name='control-chart-data'),

    url(r'^chart/(?P<board_id>[0-9]+)/burndown/$', views.show_burndown_chart,
        name='show-burndown-chart'),
    url(r'^chart/(?P<board_id>[0-9]+)/burndown-data/$',
        views.burndown_chart_data,
        name='burndown-chart-data'),

    url(r'^chart/(?P<board_id>[0-9]+)/velocity/$', views.show_velocity_chart,
        name='show-velocity-chart'),
    url(r'^chart/(?P<board_id>[0-9]+)/velocity-data/$', views.velocity_chart_data,
        name='velocity-chart-data'),

    url(r'^chart/(?P<list_id>[0-9]+)/list-history-data/$', views.list_history_data,
        name='list-history-chart-data'),

    url(r'^api/v0/card/(?P<card_id>[0-9]+)/$', views.api_get_card, name='api-get-card'),
]