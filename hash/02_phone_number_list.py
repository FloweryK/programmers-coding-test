def solution(phone_book):
    phone_book = sorted(phone_book)
    for number1, number2 in zip(phone_book, phone_book[1:]):
        return not number2.startswith(number1)


if __name__ == '__main__':
    phone_book = ['123', '456', '789']
    print(solution(phone_book))

'''
def solution(phone_book):
    for number1 in phone_book:
        for number2 in phone_book:
            if (number1 != number2) and (number1 == number2[:len(number1)]):
                return False
    return True


if __name__ == '__main__':
    phone_book = ['123', '456', '789']
    print(solution(phone_book))'''

