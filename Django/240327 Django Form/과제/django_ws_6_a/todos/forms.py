from django import forms

class TodoForm(forms.Form):
    class Meta:
        fields = '__all__'