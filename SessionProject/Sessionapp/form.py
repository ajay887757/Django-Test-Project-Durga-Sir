from django import forms

class Nameform(forms.Form):
    name=forms.CharField()

class Age(forms.Form):
    age=forms.IntegerField()

class Gf(forms.Form):
    gf=forms.CharField()
