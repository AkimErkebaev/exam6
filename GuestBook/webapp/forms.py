from django import forms
from django.forms import widgets


class GuestForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label='Title')
    author = forms.CharField(max_length=50, required=True, label='Author')
    text = forms.CharField(max_length=3000, required=True, label='Content',
                           widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}))
