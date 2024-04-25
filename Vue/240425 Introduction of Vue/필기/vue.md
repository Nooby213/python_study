# Frontend Development
- 웹 사이트와 웹 애플리케이션의 사용자 인터페이스 (UI)와 사용자 경험(UX)을 만들고 디자인 하는것

## Client-side frameworks
- 클라이언트 측에서 UI와 상호작용을 개박하기 위해 사용되는 JS기반 프레임워크
- vue, react, angular
- 필요한 이유
  - 대화형 웹사이트 (웹 애플리케이션)의 등장
  - 다루는 데이터 량의 증가

### SPA
- Single Page Application의 약자로 단일 페이지로 구성된 애플리케이션
- 하나의 HTML 파일로 시작하여, 사용자가 상호작용 할때마다 페이지 전체를 새로 로드하지 않고 화면의 필요한 부분만 동적으로 갱신
- 대부분 js 프레임워클르 사용하여 클라이언트 측에서 ui와 렌더링을 관리

### CSR
- Cilent-side Rendering
- 브라우저는 서버로부터 최소한의 HTML 페이지와 해당 페이지에 필요한 JS응답 받음
- 클라이언트 측에서 JS를 사용하여 DOM을 업데이트하고 페이지를 렌더링
- 이후 서버는 더 이상 HTML을 제공하지 않고 요청에 필요한 데이터만 응답
- Google Maps, Facebook, Instagram 등
---
- 장점
1. 빠른 페이지 전환
2. 사용자 경험
3. Frontend와 Backend의 분리
- 단점
1. 느린 초기 로드 속도
  - JS가 다운로드, 구문 분석 및 실행될 떄까지 페이지가 완전히 렌더링 되지 않기 때문
2. SEO(검색 엔진 최적화)문제
  - 페이지를 나중에 그려 나가는 것이기 때문에 검색에 잘 노출되지 않을 수 있음
  - 검색엔진 입장에서 HTML을 읽어서 분석해야 하는데 아직 콘텐츠가 모두 존재하지 않기 때문
  - Framework 사용시 해결가능

## SPA vs MPA / CSR vs SSR
- Multi Page Application
  - 여러 개의 HTML 파일이 서보로부터 각각 로드
  - 사용자가 다른 페이지로 이동할 때마다 새로운 HTML파일이 로드됨
- Server-side Rendering
  - 서버에서 화면을 렌더링 하는 방식
  - 모든 데이터가 담신 HTML을 서버에서 완성 후 클라이언트에게 전달

# Vue.js
- 사용자 인터페이스를 구축하기 위한 JS 프레임워크
1. 선억적 렌더링
  - 표준 HTML을 확장하는 템플릿 구문을 사용하여 JS를 기반으로 화면에 출력될 HTML을 선언적으로 작성
2. 반응성
  - JS 변경을 추적하고, 변경사항이 발생하면 자동으로 DOM을 업데이트
---
- 사용하는 방법
1. CDN
2. NPM 설치방식
---
```html
  <div id="app">
    <!-- 반환된 객체의 속성은 템플릿에서 동적 테스트를 렌더링한다. JS 표현식 사용가능 -->
    <h1>{{ message }}</h1>
  </div>

  // CDN 방식 연결
  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
  <script>
    // 구조분해할당
    const { createApp, ref } = Vue
    // 전달되는 객체는 Vue 컴포넌트
    // setup() 함수 내에서 선언되어야 하며 객체를 반환해야 함
    const app = createApp({
      setup() {
    // 반응형 상태(데이터)를 선언하는 함수
    // ref() .vaule 속성이 있는 ref 객체로 래핑하여 반환하는 함수
    // 인자는 어떠한 타입도 가능
        const message = ref("Hello Vue!")
        console.log(message)  // ref 객체
        console.log(message.value)  // Hello Vue!
        return {
          message
        }
      }
    })
    
    // app와 연결
    app.mount('#app')
  </script>
```