# Django URL
## URL dispatcher
- URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결(매핑)
### App URL mapping
- 각 앱에 URL을 정의하는 것
- 프로젝트와 각 앱이 URL을 나누어 관리를 편하게 하기 위함
- 'include()'
  - 프로젝트 내부 앱들의 URL을 참조할 수 있도록 매핑하는 함수
  - URL의 일치하는 부분까지 잘라내고, 남은 문자열 부분은 후속처리를 위해 include 된 URL로 전달

### Naming URL patterns
- URL에 이름을 지정하는 것
- path 함수의 name 인자를 정의해서 사용
- 'url' tag
  - 주어진 URL 패턴의 이름과 일치하는 절대 경로 주소를 반환
- 'app_name' 속성 지정
  - app_name 변수 값 설정 (app_name ='app_name')
  - herf="{% url "app_name:html" %}"