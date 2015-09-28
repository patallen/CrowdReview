from django.shortcuts import render
from django.views.generic import View, FormView
from django.http import HttpResponse
from users.forms import UserSignupForm

class UsersHomeView(View):
    """
    Main view for use with /users/ URL. This page will:
    1. List users with tabs for sorting by recent, reputation.
    2. Allow searching for users via ajax calls

    """
    def get(self, request, *args, **kwargs):
        return HttpResponse("Users Home View")

class UserSignupView(FormView):
    template_name = 'users/signup.html'
    success_url = '/'
    form_class = UserSignupForm
