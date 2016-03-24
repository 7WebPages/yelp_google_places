from django.conf.urls import url
from django.views.generic import TemplateView
from .views import *


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'api/list/$', ApiListView.as_view())
]
