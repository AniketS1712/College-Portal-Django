from django import forms
from academy.models import Students

class addinfo(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'