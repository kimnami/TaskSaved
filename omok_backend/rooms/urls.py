from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rooms import views

urlpatterns = [
    url(r'^rooms/$', views.RoomList.as_view()),
    url(r'^rooms/(?P<pk>[0-9]+)/$', views.RoomDetail.as_view()),
    url(r'^rooms/(?P<pk>[0-9]+)/players/$', views.room_players_list),
        # url(r'^rooms/(?P<pk>[0-9]+)/players/$', views.PlayerList.as_view()),
    url(r'^rooms/(?P<pk>[0-9]+)/history/$', views.HistoryList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
