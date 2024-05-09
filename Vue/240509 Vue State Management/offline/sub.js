const name = 'Alice'
const age = 20

const obj = {
  name,
  age,
  introduce() {
    console.log(`My name is ${this.name}`)
    console.log(`My age is ${this.age}years old.`)
  }
}

export const some = '정의'
export { name, age, obj }