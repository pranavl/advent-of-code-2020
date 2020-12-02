# %% Load data

with open('./input.txt', 'r') as fhandle:
    input_data = [line for line in fhandle]

len(input_data)

# %% Parse data


def parse_line(line: str):
    '''
    Parse each line and extract the values
    '''
    # Split at spaces
    parts = line.split()
    # Get the two numbers
    nums = [int(p) for p in parts[0].split('-')]
    # Get the search letter
    search_letter = parts[1][0]
    # Get the password
    password = parts[2]
    return nums, search_letter, password

# %% Part 1: Validate password function


def validate_password_1(password, search_letter, min_count, max_count) -> bool:
    '''
    Search letter must appear between min_count and max_count times (inclusive)
    '''
    letter_count = password.count(search_letter)
    return letter_count >= min_count and letter_count <= max_count

# %% Part 1: Count valid passwords


pass_count = 0
for line in input_data:
    counts, search, password = parse_line(line)
    if validate_password_1(password, search, counts[0], counts[1]):
        pass_count += 1

pass_count

# %% Part 2: Validate password function


def validate_password_2(password, search_letter, pos1, pos2) -> bool:
    '''
    Search letter must appear at pos1 XOR pos2
    '''
    def _at_pos(pw, search, pos):
        return pw[pos-1] == search
    return _at_pos(password, search_letter, pos1) ^ _at_pos(password, search_letter, pos2)

# %% Part 2: Count valid passwords


pass_count = 0
for line in input_data:
    pos, search, password = parse_line(line)
    if validate_password_2(password, search, pos[0], pos[1]):
        pass_count += 1

pass_count

# %%
