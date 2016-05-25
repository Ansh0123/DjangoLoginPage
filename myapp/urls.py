from django.conf.urls import patterns, include, url
from login.views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^admin/',admin.site.urls),
]

