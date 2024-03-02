from django import forms

from .models import Reporter

class ReporterForm(forms.ModelForm):

    class Meta:
        model = Reporter
        fields = ('name', 'stories_filed')

        