from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    description = forms.CharField(widget=forms.Textarea, required=False)
    tags = forms.CharField(max_length=255, required=False)