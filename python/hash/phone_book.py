def solution(phone_book):
    phone_book = sorted(phone_book)
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


if __name__ == "__main__":
    phone_book = ["119", "97674223", "1195524421"]	
    print(solution(phone_book))