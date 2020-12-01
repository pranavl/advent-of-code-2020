# %% Load data

with open('./input.txt', 'r') as fhandle:
    input_data = [int(line) for line in fhandle]

len(input_data)

# %% Check for a working pair

SUM_VALUE = 2020


def find_pair(input_data):
    value_set = set()
    for n in input_data:
        if SUM_VALUE - n not in value_set:
            value_set.add(n)
        else:
            return [n, SUM_VALUE - n]


value_pair = find_pair(input_data)

print(value_pair)
print('Sum:', sum(value_pair))
print('Product:', value_pair[0] * value_pair[1])

# %% Check for a working triplet


def find_triplet(input_data):
    pair_sums = {i+j: [i, j]
                 for i in input_data for j in input_data if i+j <= SUM_VALUE}
    for k, v in pair_sums.items():
        for i in input_data:
            if i + k == SUM_VALUE:
                return [v[0], v[1], i]


triplet = find_triplet(input_data)
if triplet is not None:
    print(triplet, sum(triplet), triplet[0]*triplet[1]*triplet[2])

# %%
