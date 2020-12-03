# %% Imports

import numpy as np

# %% Load data

with open('./input.txt', 'r') as fhandle:
    input_data = [line for line in fhandle]

len(input_data)

# %% Parse data


def parse_line(line: str):
    '''
    Parse each line and extract the values
    '''
    def _char_to_val(char):
        return 1 if char == '#' else 0

    return [_char_to_val(el) for el in line]


path = np.array([parse_line(line.rstrip()) for line in input_data])

print(f'Loaded {len(path)} lines')

# %% Function: Get the position on the path at each iteration


def get_line_indices(path, row_step, col_step):
    '''
    Generator function to get the position on the path based on the slope
    '''
    pos = [0, 0]
    while pos[0] < len(path):
        yield pos
        pos = [pos[0] + row_step, (pos[1] + col_step) % len(path[pos[1]])]

# %% Part 1: Count the trees you hit with a slope of right 3, down 1


tree_count = np.sum([path[pos[0], pos[1]]
                     for pos in get_line_indices(path, 1, 3)])
tree_count

# %% Part 2: Get the counts for multiple slopes

slopes = [
    [1, 1],
    [1, 3],
    [1, 5],
    [1, 7],
    [2, 1],
]


def get_count(path, row_step, col_step):
    '''
    Compute the number of trees hit going down the path at a given slope
    '''
    return np.sum([path[pos[0], pos[1]]
                   for pos in get_line_indices(path, row_step, col_step)])


counts = [get_count(path, row_step, col_step) for row_step, col_step in slopes]
print(counts)
print(np.prod(counts))

# %%
