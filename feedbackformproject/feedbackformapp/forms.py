from django import forms

# Create your models here.
class feedbackform(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        inputname = cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError("Invalid name")
        imputrollno = cleaned_data['rollno']
        if len(str(imputrollno)) !=3:
            raise forms.ValidationError("Invalid roll no")
        return inputname