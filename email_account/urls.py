from django.urls import path, re_path
from django.conf.urls import url
from . import views


app_name = 'email_account'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^activate/(?P<uid>[0-9A-Za-z_\-\']+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]
