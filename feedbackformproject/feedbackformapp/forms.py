from django import forms

# Create your models here.
class feedbackform(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        inputname = self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("Invalid name")
        return inputname