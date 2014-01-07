from writingfield import FullScreenTextarea

class BlogAdminForm(forms.ModelForm):

    class Meta:
        widgets = {
        'contentarea': FullScreenTextarea()
    }

