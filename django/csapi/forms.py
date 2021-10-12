from django import forms
from .models import OriginImage

class UploadForm(forms.ModelForm):
    class Meta:
        model = OriginImage
        fields = {'origin_image'}
