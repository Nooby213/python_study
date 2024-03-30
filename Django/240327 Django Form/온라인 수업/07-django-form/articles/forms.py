from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'placeholder':'제목을 입력하시오',
            }),
    )
    content = forms.CharField(
        label='내용',
    )
    class Meta:
        model = Article # 어떤 모델과 연동할지
        fields = '__all__' # 그 모델에서 어떤 필드를 쓸지
        # exclude = ('title',) # 제외