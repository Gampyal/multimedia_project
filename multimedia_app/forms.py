



from django import forms
from .models import MultimediaFile

class MultimediaFileForm(forms.ModelForm):
    class Meta:
        model = MultimediaFile
        fields = ['title', 'file']
