from django import forms
from .models import Memo

class MemoForm(forms.ModelForm):
    summary = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder':''}
        ))
    # memo = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'placeholder':'memo',
    #                'rows':50, 'cols':5,}
    #         )
    #         )
    class Meta:
        model = Memo
        fields = '__all__' 
        widgets = {
          'memo': forms.Textarea(attrs={'placeholder':'memo','rows':5, 'cols':50}),
        }