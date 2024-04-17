from django import forms
class urlentry(forms.Form):
    name=forms.CharField()
    url=forms.URLField()
