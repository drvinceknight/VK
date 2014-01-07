from writingfield import FullScreenTextarea
from django import forms

class BlogAdminForm(forms.ModelForm):

    class Meta:
        widgets = {
        'contentarea': FullScreenTextarea()
    }

