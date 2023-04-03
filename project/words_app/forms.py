from django import forms

class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='', max_length=200)