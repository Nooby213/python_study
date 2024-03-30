from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.

def index(request):
    return render(request, 'articles/index.html')

def create(request):
    # 생성을 위한 요청은 2가지 작업이 필요하다.
    '''
        1. 생성하기 위한 데이터를 입력할 수 있는 페이지
        2. 입력한 데이터를 토대로 실제로 데이터를 생성하는 함수
    '''
    # 사용자 요청 방식에 따라서 조건 분기
    if request.method == 'POST':    # POST 요청이 올려면 GET 요청 처리가 먼저다.
        form = ArticleForm(request.POST)
        # print(form)
        # 상속받은 ModelForm에 정의되어 있던 유효성 검사 메서드
        if form.is_valid():
            # 유효성 검사 통과 : DB에 저장 할 수 있을 것 같음
            # > Form에 field를 직접 지정하기때문에
            # 항상 모든 필드에 대한 정보를 받는건 아니다.
            # 사용자가 보내온 데이터가 정의된 field에 삽입하기 적절하다면
            form.save()
            return redirect('articles:index')
    else:
        # GET 요청이 들어왔을 때는, Articles 생성 할 수 있는 form을 렌더링
        form = ArticleForm()
    # print(form)
    context = {
        'form':form,
    }
    return render(request, 'articles/create.html', context)