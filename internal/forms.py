from  django import forms
from . import models
class uploadRecordForm(forms.ModelForm):

    class Meta:
        model=models.uploadRecord
        #fields='__all__'
        fields=['file','notice',]


