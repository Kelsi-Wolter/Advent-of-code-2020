from collections import defaultdict


f = open('boarding_passes.txt')
passes = f.read().split('\n')

# Use first 7 letters to determine row, use last 3 letters to determine
# column, multiply row * 8 and + column to get seat ID 
# find highest seat ID 


def find_row(fb_string):
    rows = {'min': 0, 'max': 128}
    
    for char in fb_string[0:6]:
        plane = rows['max'] - rows['min']
        if char == 'F':
            rows['max'] = rows['max'] - (plane/2) 
            
        if char == 'B':
            rows['min'] = rows['min'] + (plane/2)

    if fb_string[6] == 'F':
        return rows['min']
    if fb_string[6] == 'B':
        return rows['max'] - 1

def find_col(rl_string):
    cols = {'min': 0, 'max': 8}

    for char in rl_string[0:2]:
        seats = cols['max'] - cols['min']
        if char == 'L':
            cols['max'] = cols['max'] - (seats/2)
        if char == 'R':
            cols['min'] = cols['min'] + (seats/2)
        
    
    if rl_string[2] == 'L':
        return cols['min']
    if rl_string[2] == 'R':
        return cols['max'] - 1

            
def find_max_seat_id():
    max_seat_id = 0
    for boarding_pass in passes:
        row = find_row(boarding_pass[0:7])
        column = find_col(boarding_pass[7:])

        seat_id = (row * 8) + column
        
        if seat_id > max_seat_id:
            max_seat_id = seat_id

    return max_seat_id

def find_my_seat():
    passes_dict = defaultdict(list)
    for boarding_pass in passes:
        row = str(find_row(boarding_pass[0:7]))
        column = str(find_col(boarding_pass[7:]))

        if passes_dict.get(row, False) == False:
            passes_dict[row] = [column]
            
        else:
            passes_dict[row].append(column)

    for seat_row in passes_dict:
        filled_seats = len(passes_dict[seat_row])

        if filled_seats < 8:
            return passes_dict[seat_row]


