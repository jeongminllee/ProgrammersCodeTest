def solution(phone_book):
    phonebook = sorted(phone_book)
    
    for p1, p2 in zip(phonebook, phonebook[1:]) :
        if p2.startswith(p1) :
            return False
    return True