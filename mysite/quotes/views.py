from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from .models import Quote, Person

#date = timezone.localtime
class IndexView(generic.ListView):
    model = Quote
    template_name = 'quotes/index.html'
    context_object_name = 'quote_list'
