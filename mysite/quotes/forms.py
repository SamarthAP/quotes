from django import forms

class QuoteForm(forms.Form):
    quote = forms.CharField(label='Quote:')
    name = forms.CharField(label='Name:')