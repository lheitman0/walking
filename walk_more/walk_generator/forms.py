from django import forms

class RouteForm(forms.Form):
    location = forms.CharField(label='Enter your location', max_length=100)
    time = forms.IntegerField(label='Enter the walking time (in minutes)')