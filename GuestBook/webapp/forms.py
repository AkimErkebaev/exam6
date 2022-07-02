from django import forms
from django.forms import widgets


class GuestForm(forms.Form):
    author = forms.CharField(max_length=50, required=True, label='Author')
    email = forms.CharField(max_length=50, required=True, label='Email')
    text = forms.CharField(max_length=3000, required=True, label='Text',
                           widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}))
