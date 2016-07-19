from django.conf.urls import url
from logInOut.views import *


urlpatterns = [
        url(r'^in/$', login),
        url(r'^out/$', logout),
        ]