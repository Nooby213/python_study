def rental_book(name, book):
    print(f'남은 책의 수 : {decrease_book(book)}')
    print(f'{name}님이 {book}권의 책을 대여하였습니다.')

number_of_book = 100

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    return number_of_book

rental_book('홍길동',3)