# World Wide Web
- 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간
## Web
- web site, web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술
## Web site
- 여려 개의 Web page가 모인 것으로 사용자들에게 정보나 서비스를 제공하는 공간
## Web page
- HTML, CSS 등의 웹 기술을 이용하여 만들어진, Web site를 구성하는 하나의 요소
- HTML : structure
- CSS : styling
- Javascript : behavior
---
### HTML
- Hyper Text Markup Language
- 웹 페이지의 **의미**와 **구조**를 정희하는 언어
---
#### Hypertext (링크)
- 웹 페이지를 다른 페이지로 연결하는 링크
- 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
---
#### Markup Language
- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- 예) HTML, Markdown
---
#### HTML 구조
- \<!DOCTYPE html>
  - 해당 문서가 html로 문서라는 것을 나타냄
- \<html>\</html>
  - 전체 페이지의 콘텐츠를 포함
- \<title>\</title>
  - 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
- \<head>\</head>
  - HTML 문서에 관련된 설명, 설정 등
  - 사용자에게 보이지 않음
- \<body>\</body>
  - 페이지에 표시되는 모든 컨텐츠

- html

![html](/html.JPG)

- HTML Element(요소)

![contents](/contents.JPG)

- HTML Attributes(속성)

![attributes](/attributes.JPG)
---
#### HTML Text structure
- Heading & Paragraphs
  - h1~6, p
- Lists
  - ol, ul, li
- Emphasis & Importance
  - em, strong
---
### CSS
- Cascading Style Sheet
- 웹 페이지의 **디자인**과 **레이아웃**(배치)을 구성하는 언어

![css구문](/css.JPG)
---
### CSS Selectors
- HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자
- 기본 선택자
  - 전체("*") 선택자
    - HTML 모든 요소를 선택
  - 요소(tag) 선택자
    - 지정한 모든 태그를 선택
  - 클래스(class) 선택자
    - '.', 주어진 클래스 속성을 가진 모든 요소를 선택
  - 아이디(id) 선택자
    - '#', 주어진 아디이 속성을 가진 요소 선택
    - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
  - 속성(attr) 선택자 등
- 결합자 (Combinators)
  - 자손 결합자(" "(space))
    - 첫 번째 요소의 자손 요소들 선택
    - 예) p span은 \<p> 안에 있는 모든 \<span>를 선택(하위 레벨 상관 없이)
  - 자식 결합자(">")
    - 첫 번째 요소의 직계 자식만 선택
    - 예) ul > li은 \<ul> 안에 있는 몯느 \<li>를 선택 (한 단계 아래 자식들만)
---
### Specificity 명시도
- 결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘
- CSS Selector에 가중치를 계산하여 어떤 스타일을 적용할지 결정
- 동일한 요소를 가리키는 2개 이상의 CSS규칙이 있는 경우 가장 높은 명시도를 가진 Selector가 승리하여 스타일이 적용됨
- 명시도 높은 순
1. Importance
   - !important
   -  다른 우선순위 규칙보다 우선하여 적용하는 키워드
   -  사용권자하지 않음
2. Inlilne 스타일
3. 선택자
   - id 선택자 > class 선택자 > 요소 선택자
4. 소스 코드 선언 순서
---
### Cascade 계단식
- 한 요소에 동일한 가중치를 가진 선택자가 적용될 때 CSS에서 마지막에 나오는 선언이 사용됨
- 되도록 class만 사용할 것
---
### CSS 상속
- 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임
- 상속 되는 속성
  - Text 관련 요소(font, color, text-align), opacity, visibility 등
- 상속 되지 않는 속성
  - Box model 관련 요소(width, height, border, box-sizing ...)
  - position 관련 요소(position, top/right/bottom/left, z-index ...) 등
---
#### HTML 관련 사항
- 요소(태그) 이름은 대소문자를 구분하지 않지만 **소문자** 사용을 권장
- 속성의 따옴표는 작은 타옴표와 큰 따옴표를 구분하지 않지만 **큰 따옴표** 권장
- HTML은 프로그래밍 언어와 달리 에러를 반환하지 않기 때문에 작성 시 주의