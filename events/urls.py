"""events URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from mainApp.views import *



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^current/$', events_current),
    url(r'^coming/$', events_coming),
    url(r'^recent/$', events_recent),
    url(r'^archiv/$', events_archiv),
    url(r'^event/([0-9]+)$', show_event),
    url(r'^events/bycat/([0-9]+)$', index),
    url(r'^places/$', places),
    url(r'^place/([0-9]+)$', show_place),
    url(r'^places/bycat/([0-9]+)$', places),
    url(r'^articles/$', articles),
    url(r'^article/([0-9]+)$', show_article),
    url(r'^log/', include('logInOut.urls')),
    url(r'^register/', include('register.urls')),
    url(r'^cadmin/', include('customAdmin.urls')),
]
