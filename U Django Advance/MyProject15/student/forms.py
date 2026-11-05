from django import forms
from .models import Student

class Studentform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','age','email']

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 18:
            raise forms.ValidationError("Age must be atlease 18")
        return age
    