# %% Load data

with open('./input.txt', 'r') as fhandle:
    input_data = [line.strip() for line in fhandle]

len(input_data)

# %% Part 1: Parse data


def parse_data(data):
    '''
    Parse data and return a list of all answers in a group
    '''
    parsed = [[]]
    for line in data:
        split_line = list(line)
        if len(split_line) > 0:
            # Add to a group
            parsed[-1] += split_line
        else:
            # Add a new group
            parsed.append([])
    return parsed


groups = parse_data(input_data)
print(f'Loaded {len(groups)} groups')

# %% Part 1: Count unique YES's in each group

sum([len(set(g)) for g in groups])


# %% Part 2: Parse data

class Group(object):

    def __init__(self):
        # Dictionary of answers: number of occurrences
        self.answers = {}
        # Number of members in the group
        self.num_members = 0

    def add_answers(self, answers: [str]):
        '''
        Add one person's answers to the group's record
        '''
        for a in answers:
            self.answers[a] = self.answers.get(a, 0) + 1
        self.num_members += 1

    @property
    def yes_count(self):
        '''
        Count the number of answers
        that were answered YES by everyone in the group
        '''
        return sum([v == self.num_members for v in self.answers.values()])


def parse_data(data):
    '''
    Parse data and return a list of answers in each group and group count
    '''
    parsed = [Group()]
    for line in data:
        split_line = list(line)
        if len(split_line) > 0:
            # Add to a group
            parsed[-1].add_answers(split_line)
        else:
            # Add a new group
            parsed.append(Group())
    return parsed


groups = parse_data(input_data)
print(f'Loaded {len(groups)} groups')

# %% Part 2: Count the number of YES's answered by everyone in a group

sum([g.yes_count for g in groups])

# %%
