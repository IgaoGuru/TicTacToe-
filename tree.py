class Tree:

    value = None
    left = None
    right = None

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def generate_binary_tree(elements:list):
    if len(elements) == 0:
        return None
    if len(elements) == 1:
        return Tree(elements[0])

    half = int(len(elements) / 2)

    left = generate_binary_tree(elements[:half])
    right = generate_binary_tree(elements[half+1:])

    big_tree = Tree(elements[half], left, right)
    print("Tree successfully generated")
    return big_tree


def tree_has_element(tree:Tree, element:int):
    if tree is None:
        return False
    if tree.value == element:
        return True
    if element < tree.value:
        return tree_has_element(tree.left, element)
    else:
        return tree_has_element(tree.right, element)


def count_nodes(tree):#-> int
    n = 0
    n += 1
    if tree.right != None:
        n += count_nodes(tree.right)
    if tree.left != None:
        n += count_nodes(tree.left)
    return n


def count_leaves(tree): #-> int
    n = 0
    if tree.right == None and tree.left == None:
        n += 1
        return n
    elif tree.right != None:
        n += count_leaves(tree.right)
    if tree.left != None:
        n += count_leaves(tree.left)
    return n


def print_tree(tree, tabs = ""): #-> (just prints)

    print(tabs + str(tree.value))
    tabs += " "
    if tree.right != None:
        print_tree(tree.right, tabs)
    if tree.left != None:
        print_tree(tree.left, tabs)
    return

def count_greater_than(tree, value): #-> int
    n = 0
    if tree.value > value:
        n += 1
    if tree.right != None:
        n += count_greater_than(tree.right, value)
    if tree.left != None:
        n += count_greater_than(tree.left, value)
    return n


def count_smaller_than(tree, value): #-> int
    n = 0
    if tree.value < value:
        n += 1
    if tree.right != None:
        n += count_smaller_than(tree.right, value)
    if tree.left != None:
        n += count_smaller_than(tree.left, value)
    return n


def count_greater_than_pruning(tree, value, block = 0): #-> int
    n = 0
    if tree == None:
        return 0
    print(tree.value)
    #pruning left tree
    if tree.value <= value:
        n += count_greater_than_pruning(tree.right, value, block)
    else:
        n += 1
        n += count_greater_than_pruning(tree.left, value, block)
        n += count_greater_than_pruning(tree.right, value, block)
    return n

#testing pad

elements = list(range(1, 10))

tree = generate_binary_tree(elements)

a = count_greater_than_pruning(tree, 6)
print(a)


