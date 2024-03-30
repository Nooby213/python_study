from django import forms
from .models import Article
'''
    둘다 class에 상속 시켜줄 class라는 점
    class > PascalCase
    Form vs ModelForm
    Form > Model에 대한 정보가 없는 Form을 위한 클래스

    ModelForm > Model에 대한 정보가 있는 Form을 위한 클래스
'''
# class AricleForm(forms.Form):
#     # 모델에 대한 정보 없이 Form을 구성하려면?
#     # 적절한 Filed들을 내가 직접 작성해 줘야한다.
#     '''
#         HTML에서 쓸 form 태그를 구성해주는 class인데
#         field에 대한 정보가 없으면, input tag 뭘 써야 할지 알 수 없다.
#         그래서 그 field들 내가 정의한다.
#         정의하는 방법은 django Model 정의하는거랑 똑같다.    
#     '''
#     # title = forms.CharField(max_length=10)
#     # content = forms.CharField()
#     # is_hidden = forms.BooleanField()
#     pass

class ArticleForm(forms.ModelForm):
    # HTML에서 사용할 form 태그를 구성할 필드 정보를
    # model로부터 받아온다.
    class Meta:
        model = Article
        fields = '__all__'