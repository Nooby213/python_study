# HTML 'form'
- 지금까지 사용자로부터 데이터를 받기위해 활용한 방법
- 비정상적 혹은 악의적인 요청을 필터링 할 수 없음
- 유효한 데이터인지에 대한 확인이 필요

## 유효성 검사
- 수집한 데이터가 정확하고 유효한지 확인하는 과정
- 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야함
- 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용

# Django Form
- 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구
- 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공


## Form
- HTML 'input' element의 표현 담당

- Form
  - 사용자 입력 데이터를 DB에 저장하지 않을 때
  - 로그인 등

```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    # widget 으로 스타일 변경
    content = forms.CharField(widget=forms.Textarea)
  ```
  

- ModelForm
  - 사용자 입력 데이터를 DB에 저장해야 할 때
  - 게시글 작성, 회원가입
  - Model과 연결된 Form을 자동으로 생성해주는 기능을 제공
  - Form + Model

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # Meta class
    # ModelFrom의 정보를 작성하는 곳
    class Meta:
        model = Article # 어떤 모델과 연동할지
        fields = '__all__' # 그 모델에서 어떤 필드를 쓸지
        # exclude = ('title',) # 제외
```

