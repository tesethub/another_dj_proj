from django.forms import ModelForm, HiddenInput
from mainApp.models import Registration

class MyForm(ModelForm):

    class Meta:
        model = Registration
        fields=['name', 'email']
        #widgets={
            #'subject':HiddenInput()
       # }