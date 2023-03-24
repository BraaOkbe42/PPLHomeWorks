##level 0
def make_tree(root, left, right):
    ''' here we save the data we recieve then we save it in dispatch function the we return the dispatch function'''
    def dipatch(i):
        if i == 0 : return root
        if i == 1 : return left
        if i == 2 : return right
    return dipatch

##level 1
def value(tree):
    ''' return the root'''
    return tree(0)

def left(tree):
    '''return the left node ''' 
    return tree(1)

def right(tree):
    ''' return the right node''' 
    return tree(2)

##level 2
def print_tree(tree):
    '''here we print the tree in-order'''
    if value(tree) == None: return
    if left(tree) != None:
        print_tree(left(tree))
    print(value(tree), end=' ')
    if right(tree) != None:
        print_tree(right(tree))



def min_value_help(tree):
    ''' first Initialize the result with the value of the current node, second Get the minimum value in the left subtree, if it exists
last Get the minimum value in the right subtree, if it exists
'''
    if tree == None: return

    res = value(tree)
    leftmin = min_value_help(left(tree))
    if leftmin is not None and leftmin < res:
        res = leftmin
    rightmin = min_value_help(right(tree))
    if rightmin is not None and rightmin < res:
        res = rightmin
    return res

def min_tree(tree):
    ''' using min_value_help as a helping function'''
    print(min_value_help(tree))



def mirror_tree(tree):
    '''we mirrorize the tree using recursion  '''
    if tree is None:
        return 
    lefttree = mirror_tree(left(tree))
    righttree=mirror_tree(right(tree))
    return make_tree(value(tree),righttree,lefttree)


tree = make_tree(12,make_tree(6,make_tree(8,None,None),None),make_tree(7,make_tree(2,None,None),make_tree(15,None,None)))
