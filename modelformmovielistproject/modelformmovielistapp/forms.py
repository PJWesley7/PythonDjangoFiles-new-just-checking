from django import forms
from modelformmovielistapp.models import movielist

class movieform(forms.ModelForm):
    class Meta:
        model = movielist
        fields = '__all__'