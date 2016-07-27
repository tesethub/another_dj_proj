from django.conf.urls import url
from comments.views import *


urlpatterns = [
        url(r'^add/$', add_comment),
        ]