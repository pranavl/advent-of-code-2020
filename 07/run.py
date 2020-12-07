# %% Load data

with open('./input.txt', 'r') as fhandle:
    input_data = [line.strip() for line in fhandle]

len(input_data)

# %% Function: Parse data


def parse_bag_rule(rule):
    '''
    Helper function: Parse a part of a rule that looks like:
    - "1 vibrant gold bag"
    - "2 wavy aqua bags"
    - "no other bags"

    Return a list of tuples (number, color)
    '''
    split_rule = rule.strip().split()
    return (int(split_rule[0]), ' '.join(split_rule[1:-1]))


def parse_line(line):
    '''
    Parse a rule
    '''
    # Replace "no" with a 0
    line = line.replace('no ', '0 ')
    # Split a rule into the parent bag and sub bags
    split_rule = line[0:-1].split('contain')
    # Get the parent bag color
    parent = ' '.join(split_rule[0].strip().split()[0:-1])
    # Get the sub bag rules
    child_rules = split_rule[1].strip().split(', ')
    children = [parse_bag_rule(rule) for rule in child_rules]
    # Filter out 0 children
    children = [child for child in children if child[0] > 0]
    return parent, children

# %% Parse all data


rules = [parse_line(line) for line in input_data]
print(len(rules), 'rules')

# %% Class: Graph of bag rules


class BagNode(object):
    def __init__(self, color):
        self.color = color
        # List of parent colors
        self.parents: [str] = []
        # List of children (number needed, color)
        self.children: [(int, str)] = []


class BagGraph(object):
    def __init__(self):
        self.nodes = {}

    def get_node(self, color: str) -> BagNode:
        '''
        Get a node with a specific color. Create it if it doesnt exist
        '''
        if color not in self.nodes:
            self.nodes[color] = BagNode(color)
        return self.nodes[color]

    def add_rule(self, parent_color: str, rules: [(int, str)]):
        '''
        Add a rule.
        - Add nodes to the graph dictionary
        - Point parents and children nodes at each other
        '''
        parent = self.get_node(parent_color)
        for rule in rules:
            child = self.get_node(rule[1])
            parent.children.append(rule)
            child.parents.append(parent_color)

# %% Create a graph of bag rules


graph = BagGraph()
for rule in rules:
    graph.add_rule(rule[0], rule[1])

print(len(graph.nodes), 'nodes in the graph')

# %% Part 1: Find all colors that eventually let you carry a "shiny gold" bag

bag_color = 'shiny gold'

visited = []


def find_all_parents(bag_graph: BagGraph, child_color: str) -> [str]:
    '''
    Find all color bags that can eventually contain a given color
    '''
    child_node = bag_graph.get_node(child_color)
    for parent_color in child_node.parents:
        if parent_color not in visited:
            visited.append(parent_color)
            find_all_parents(bag_graph, parent_color)


find_all_parents(graph, bag_color)
print(len(visited), f'other bags can eventually contain a {bag_color} bag')

# %% Part 2: Count how many bags must be carried in your bag

bag_color = 'shiny gold'


def count_children(bag_graph: BagGraph, parent_color: str) -> int:
    '''
    Count the number of children in a bag of a given color
    '''
    parent_node = bag_graph.nodes[parent_color]
    children = parent_node.children
    if len(children) == 0:
        return 0
    return sum([child[0] + child[0] * count_children(bag_graph, child[1]) for child in children])


print(count_children(graph, bag_color),
      f'bags needed inside a {bag_color} bag')

# %%
