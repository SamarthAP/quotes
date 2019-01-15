from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Quote, Person
from .forms import QuoteForm

#date = timezone.localtime
class IndexView(generic.ListView):
    model = Quote
    template_name = 'quotes/index.html'
    context_object_name = 'quote_list'

    def people(self):
        return Person.objects.all()

    def post(self, request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            name = request.POST['name']
            text = request.POST['quote']
            if Person.objects.filter(name=name).exists():
                print('exists')
                quote = Quote(person=Person.objects.get(name=name), text=text, date=timezone.localtime())
                quote.save()
            else:
                print('doenst exist')
                person = Person(name=request.POST['name'])
                person.save()
                quote = Quote(person=person, text=text, date=timezone.localtime())
                quote.save()
        # if a GET (or any other method) we'll create a blank form
        else:
            form = QuoteForm()

        return redirect(reverse_lazy('quotes:index'))        
