# pjt 06

## 버전2_영화

## 어려웠던 점
1. 네비바 만드는점
- 로그아웃 상태에서 프로필, 로그아웃 버튼이 나오면 안되었다.
- 그렇기에 로그인 상태에서는 프로필, 로그아웃 버튼이,
- 로그아웃 상태에서는 회원가입, 로그인 버튼이 나와야 했다.


## 해결방법
```html
{% if user.is_authenticated %}
  <form class="nav-item" action="{% url "accounts:profile" user.username %}" method="POST">
    {% csrf_token %}
    <input class="btn btn-link nav-link" type="submit" value="프로필">
  </form>
  <form class="nav-item" action="{% url "accounts:logout" %}" method="POST">
    {% csrf_token %}
    <input class="btn btn-link nav-link" type="submit" value="로그아웃">
  </form>
{% else %}
  <form class="nav-item" action="{% url "accounts:signup" %}" method="POST">
    {% csrf_token %}
    <input class="btn btn-link nav-link" type="submit" value="회원가입">
  </form>
  <form class="nav-item" action="{% url "accounts:login" %}" method="POST">
    {% csrf_token %}
    <input class="btn btn-link nav-link" type="submit" value="로그인">
  </form>
{% endif %}
```

- {% if user.is_authenticated %} 를 통해서 로그인 상태와 비로그인 상태를 나누었다.
- form을 사용하여 로그아웃, 회원가입, 프로필 기능을 수행하였다.


2. 프로필 기능 구현하기
- 나를 팔로잉, 팔로워 하는 사람들 숫자 구하는 것이 어려웠다.

## 해결방법
```html
<p>팔로워: {{person.followers.all|length}}</p>
<p>팔로잉: {{ person.followings.all|length}}</p>
```
length를 이용해서 해결 할 수 있었다.



3. 영화 create 구현하기
 
```python
# movies/views.py
@require_http_methods(["GET", "POST"]) 
def create(request):
  if request.method == "POST":
    form = MovieForm(request.POST)
    if form.is_valid():
      movie = form.save(commit=False)
      movie.user = request.user
      form.save()
      return redirect('movies:detail', movie.pk)
  elif request.method == "GET":
    form = MovieForm()
  context = {
    'form' : form,
  }
  return render(request, 'movies/create.html', context)

```
에서 movie에 form.save(commit=False) 객체를 변수지정하지 않고 그냥 했더니 null constraint 오류가 발생하였다.

시간에 비해 구현해야 될 기능이 많았는데 시간분배를 잘 못한거 같다.