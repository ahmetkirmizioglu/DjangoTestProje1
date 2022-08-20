from django.conf.urls import url
from .views import *

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', login_view, name="login"),
    url(r'^register/$', register_view, name="register"),
    url(r'^profile/$', profile_view, name="profile"),
    url(r'^change_password/$', change_password_view.as_view(), name="change_password"),
    #url(r'^(?P<id>\d+)/profile/$', profile_view, name='profile'),
    url(r'^logout/$', logout_view, name="logout"),
]