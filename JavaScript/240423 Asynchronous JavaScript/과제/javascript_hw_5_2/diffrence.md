# 동기
- 동기적인 코드는 위에서 아래로 순차적으로 실행된다.
```js
console.log('첫 번째 작업 시작')
console.log('두 번째 작업 시작')
console.log('세 번째 작업 시작')
```
# 비동기
- 비동기적인 코드는 특정 함수나 코드가 완료될 때까지 기다리지 않고 다음 작업을 시작한다
```js
console.log('첫 번째 작업 시작')

setTimeout(function() {
    console.log('두 번째 작업 시작')
}, 2000)

console.log('세 번째 작업 시작')
```