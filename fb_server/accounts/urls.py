from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', auth_views.login, name='login',kwargs={
            'template_name': 'login.html'
        }),
    url(r'^register/$', views.AccountRegister.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)