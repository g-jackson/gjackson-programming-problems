test_input = '''FBFBBFFRLR'''


def find_seat(record):
    max_val = 128
    min = 0
    for char in record[:7]:
        if char == 'F':
            max_val -= (max_val - min) // 2
        else:
            min += (max_val - min) // 2
        # print(char, min, max_val)
    row = min
    max_val = 8
    min = 0
    for char in record[-3:]:
        if char == 'L':
            max_val -= (max_val - min) // 2
        else:
            min += (max_val - min) // 2
        # print(char, min, max_val)
    column = min
    return row, column


def a(inputs):
    max_id = 0
    row, column = 0, 0
    for record in inputs:
        row, column = find_seat(record)
        # print(row, column)
        max_id = max(max_id, (row * 8) + column)
    return max_id


def b(inputs):
    seat_ids = [False] * 128 * 8
    for record in inputs:
        row, column = find_seat(record)
        seat_ids[(row * 8) + column] = True
    # print(seat_ids)

    start = False
    for seat in range(len(seat_ids)):
        if seat_ids[seat]:
            start = True
        if not seat_ids[seat] and start:
            return seat


with open('inputs/05in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split('\n')

print(a(inputs))
print(b(inputs))
