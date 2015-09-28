from django.conf.urls import url
from django.views.generic import TemplateView, View
from users.views import UsersHomeView, UserSignupView

urlpatterns = [
    url(r'^$', UsersHomeView.as_view(), name='users_view'),
    url(r'^signup/$', UserSignupView.as_view(), name='user_signup_view'),
]
