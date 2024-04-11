def time_(s) :
    hh, mm = s.split(":")
    return int(hh) * 60 + int(mm)

def solution(book_time):
    events = []
    for start, end in book_time :
        start_time = time_(start)
        end_time = time_(end) + 10
        events.append((start_time, 'start'))
        events.append((end_time, 'end'))
        
    events.sort()
    
    rooms = 0
    curr = 0
    
    for _, event in events :
        if event == 'start' :
            curr += 1
            rooms = max(rooms, curr)
            
        else :
            curr -= 1
            
    return rooms