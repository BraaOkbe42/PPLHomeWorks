from functools import reduce

def avg_salary(seq):
    '''first we extract all the salaries then we calculate the summition

    of it, then we calculate the lenght of every new sequence
    last we take the letters of every sequence and we attatch it with the total'''
    total= tuple(map(sum, map(lambda x: x,map(lambda x: x[1], seq))))
    lenght = tuple(map(lambda x: len(x[1]), seq))
    letters = tuple(map(lambda x: x[0], seq))
    return tuple(map(lambda x, y: (x,y), letters, map(lambda x, y: x / y, total, lenght)))



def add_bonus(seq, bonus):
    ''' adding the bonus that we recieved to the sequence  '''
    addedbonus = tuple(map(lambda x, y : list(map(lambda z: z + y[1] if x[0] == y[0] else None, x[1])),seq, bonus))
    result = tuple(map(lambda x: (min(x), max(x), sum(x)/len(x)), addedbonus))
    return result




salaries = (('a', [12675, 7876, 8765])), ('b', [9500, 6987]), ('c', [7500, 4576]),('d', [11654])
bonus = (('a', 1000), ('b', 2000), ('c', 900), ('d', 3500))
