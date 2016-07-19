from django.conf.urls import url
from register.views import *


urlpatterns = [
        url(r'^$', register),
        ]