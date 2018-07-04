from django import forms

from my_app.models import Demo


class DemoCreateForm(forms.ModelForm):
    class Meta:
        model = Demo
        fields = ['text']