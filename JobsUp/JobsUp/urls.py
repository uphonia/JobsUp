"""JobsUp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
admin.autodiscover()

import jobs.views

urlpatterns = [
	url(r'^$', jobs.views.index, name = 'index'),
	url(r'^sign_up/$', jobs.views.sign_up, name = 'signup'),
	url(r'^log_in/$', jobs.views.log_in, name = 'login'),
	url(r'^log_out/$', jobs.views.log_out, name = 'logout'),
	url(r'^edit_profile/$', jobs.views.edit_profile, name = 'edit'),
	url(r'^view_map/$', jobs.views.view_map, name = 'mapview'),
    url(r'^view_profile/$', jobs.views.view_profile, name = 'profile'),
    url(r'^admin/', admin.site.urls),
]
