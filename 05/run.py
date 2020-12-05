# %% Load data

with open('./input.txt', 'r') as fhandle:
    input_data = [line.strip() for line in fhandle]

len(input_data)

# %% Functions

TOTAL_ROWS = 128
TOTAL_COLS = 8


def get_position_code(seat) -> (str, str):
    '''
    Split the seat code into the two parts
    '''
    return seat[0:7], seat[7:]


def get_side(char) -> int:
    '''
    Convert a character to an index corresponding to a side.
    0 is front/left, 1 is back/right
    '''
    if char in ['F', 'L']:
        return 0
    if char in ['B', 'R']:
        return 1
    raise ValueError(f'Unknown character: {char}')


def bsp(code, seat_range) -> int:
    '''
    Binary Space Partitioning:
    Recursively compute the seat position
    '''
    # Split the seat code into the different directions
    first, rest = code[0], code[1:]
    # Get the half specified in the code
    side_idx = get_side(first)
    mid = int(len(seat_range)/2)
    seat_split = (seat_range[0:mid], seat_range[mid:])
    sel_side = seat_split[side_idx]
    # Recursively search, if there is more in the code
    if len(rest) > 0:
        return bsp(rest, sel_side)
    # Otherwise, return the position
    return sel_side[0]


def get_row_col(seat_code) -> (int, int):
    '''
    Convert a seat code into a row and column
    '''
    row_code, col_code = get_position_code(seat_code)
    return bsp(row_code, range(TOTAL_ROWS)), bsp(col_code, range(TOTAL_COLS))


def compute_seat_id(row, col) -> int:
    '''
    Compute a seat ID from the position
    '''
    return row * 8 + col

# %% Test that it works

# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.


seat_code = 'BBFFBBFRLL'
row_pos, col_pos = get_row_col(seat_code)
print(seat_code, row_pos, col_pos, compute_seat_id(row_pos, col_pos))

# %% Part 1: Compute the maximum seat id for all boarding passes

seat_ids = []
for seat in input_data:
    row_pos, col_pos = get_row_col(seat)
    seat_ids.append(compute_seat_id(row_pos, col_pos))

max(seat_ids)

# %% Part 2: Find your seat id

for i in range(min(seat_ids), max(seat_ids)):
    if i not in seat_ids and i+1 in seat_ids and i-1 in seat_ids:
        print(i)

# %%
