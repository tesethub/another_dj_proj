from django.conf.urls import url
from signToEvents.views import *



urlpatterns = [
        url(r'^([0-9]+)$', registrate),
        url(r'^bylink/$', reg_by_link),
        url(r'^confirm/([0-9a-z]+)/$', confirm),
        ]