from django.conf.urls import url
from customAdmin.views import *


urlpatterns = [
        url(r'^$', index),
        url(r'^del/$', delitem),
        url(r'^edit/$', show_form),
        url(r'^save/$', save_form),
        ]