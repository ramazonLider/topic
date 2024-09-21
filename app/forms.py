from django import forms

class TopicSearchForm(forms.Form):
    query = forms.CharField(label='Search Topics', max_length=100)
