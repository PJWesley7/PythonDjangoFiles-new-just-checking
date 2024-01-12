from django import forms

class additemform(forms.Form):
    name=forms.CharField()
    quantity=forms.IntegerField()