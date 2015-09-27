from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import HttpResponse

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Yup')
