from django.shortcuts import render
from django.views.generic.base import TemplateView
from django .http import HttpResponse, HttpResponseRedirect

# Create your views here.

class BaseView(TemplateView):
	template_name = 'qpl/base.html'