import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useMyCounterStore = defineStore('counter', () => {
  let id = 0
  const todos = ref([
  ])
  const addTodo = function (todoText) {
    todos.value.push({
      id: id++,
      text: todoText,
      isDone: false
    })
  }

  const deleteTodo = function (todoId) {
    // console.log(todoId)
    // todos 상태에서 인자로 전달된 todo를 찾아서 삭제한 todos를 전달해야됌
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    console.log(index)
    // 찾은 인덱스를 활용하여 todos에서 삭제 후 새로운 todos로 교체
    todos.value.splice(index, 1)
  }

  const updateTodo = function (todoId) {
    // 전달 받은 todoId를 활용
    // todos 배열을 순회하면서 id가 일치하면 isDone을 반대로 바꾸고
    // 변경된 새로운 배열을 반환
    todos.value = todos.value.map((todo) => {
      if (todo.id === todoId) {
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }

  const doneTodoCount = computed(() => {
    const doneTodos = todos.value.filter((todo) => todo.isDone)
    return doneTodos.length
  })
  return {
    todos, doneTodoCount,
    addTodo, deleteTodo, updateTodo
  }
}, { persist: true })






/*
export const useCounterStore = defineStore('counter', () => {
  // 공유하지 않는 private한 상태 속성을 가지지 않음

  // 반응형 상태 ref() === state
  const count = ref(0)
  // conputed() === getters 
  const doubleCount = computed(() => count.value * 2)
  // function() === actions
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
}) // 3번째 인자로 plugin이 들어온다. 
// 애플리케이션의 상태 관리에 필요한 추가 기능을 제공하거나 확장하는 도구나 모듈
// 설치 이후 별도 설정을 통해 추가되고 상태관리를 간편하고 유연하게 만들어줌
*/