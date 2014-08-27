from django import forms
from models import UploadFile, BatchJob

#for dropzone:   
class UploadFileForm(forms.ModelForm):   
    class Meta:
        model = UploadFile

#     file = forms.FileField()

# class UploadFileForm(forms.Form):
# #     title = forms.CharField(max_length=50)
#     file = forms.FileField()

class BatchForm(forms.ModelForm):
    class Meta:
        model = BatchJob