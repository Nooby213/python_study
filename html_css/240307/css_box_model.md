# CSS Box Model
- 모든 HTML 요소를 사각형 박스로 표현하는 개념
- 내용(content), 안쪽 여백(padding), 테두리(border), 외부 간격(margin)으로 구성되는 개념
![박스구성요소](/240307/box구성요소.JPG)
## 박스 타입
- Block & Inline
### Normal flow
- CSS를 적용하지 않았을 경우 웹페이지 요소가 기본적으로 배치되는 방향
#### Block
- 아래로
- 항상 새로운 행으로 나뉨
- width와 height 속성을 사용하여 너비와 높이를 지정할 수 있음
- 기본적으로 width 속성을 지정하지 않으면 박스는 inline 방향으로 사용가능한 공간을 모두 차지함(너비를 사용가능한 공간으니 100%로 채우는 것)
- 대표적 block 타입 태그
  - h1~6, p, div
#### Inline
- 오른쪽으로
- 새로운 해응로 나뉘지 않음
- width와 height 속성을 사용할 수 없음
- 수직방향
  - padding, margins, borders가 적용되지만 다른 요소를 밀어낼 수는 없음
- 수평방향
  - padding, margins, borders가 정용되어 다른 요소를 밀어낼 수 있음
- 대표적인 inline 타입 태그
  - a, img, span
![정렬](/240307/정렬.JPG)
#### 기타 display 속성
1. inline-block
  - inline과 block 요소 사이의 중간 지점을 제공하는 display 값
  - block 요소의 특징을 가짐
    - width 및 속성 사용 가능
    - padding, margin 및 border 로 인해 다른 요소가 밀려남
  - 요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이를 적용하고 싶은 경우에 사용
2. none
  - 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
#### shorthand
- border
  - border-width, border-style, border-color
  - border: 2px solid black;
- margin & padding
  - 4개 - 상우하좌
  - 3개 - 상/좌우/하
  - 2개 - 상하/좌우
  - 1개 - 모든 범위
  - 상하 마진은 큰 마진만큼만 적용된다.
---
## CSS Layout
- 각 요소의 위치와 크기를 조정하여 웹 페이지의 디자인을 결정하는것
- display, position, float, flexbox 등

### CSS Position
- 요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것
- 다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 등
- 유형
 1. static
  - 기본값
  - 요소를 normal flow에 따라 배치
 2. relative
  - 요소를 normal flow에 따라 배치
  - 자기 자신을 기준으로 이동
  - 요소가 차지하느 공간은 static일 때와 같음
 3. absolute
  - 요소를 normal flow에서 제거
  - 가장 가까운 relative 부모 요소를 기준으로 이동
  - 문서에서 요소가 차지하는 공간이 없어짐
 4. fixed
  - 요소를 normal flow에서 제거
  - 현재 화면 영역(viewport)을 기준으로 이동
  - 문서에서 요소가 차지하는 공간이 없어짐
 5. sticky
  - 요소를 normal flow에 따라 배치
  - 요소가 일반적인 문서 흐름에 따라 배치되거나 스크롤이 특정 임계점에 도달하면 그 위치에서 고정된(fixed)
  - 만약 다음 sticky요소가 나오면 다음 sticky요소가 이전 sticky요소의 자리를 대체
  - 이전 sticky요소가 고정되어 있던 위치와 다음 sticky요소가 고정되어야 할 위치가 겹치기 때문
### Z-index
- 요소가 겹쳤을 때 어떤 요소 순으로 위에 나타날 지 결정
- 정수 값을 사용해 Z축 순서를 지정
- 더 큰 값을 가진 요소가 작은 값의 요소를 덮음
### position
- 전체 페이지에 대한 레이아웃을 구성하는 것이 아닌 페이지 특정 항목의 위치를 조정하는 것
### CSS Flexbox
- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
- 공간 배열 & 정렬
- 구성요소
![flexbox](/240307/flexbox.JPG)