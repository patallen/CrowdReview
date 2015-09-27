from django.conf.urls import url
from django.views.generic import TemplateView, View
from reviews.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index_view'),
]


