'''This will be a collection of our first set of functions'''
def max_of_three(arg1,arg2,arg3):
    "this function takes in three arguments and returns the largest value"
    if arg1 > arg2 and arg1>arg3:
        return arg1
    elif arg2 > arg3:
        return arg2
    else:
        return arg3
def list_ends(L) :
    '''this function takes in a list and returns a new list with the first and last entry'''

    return[L[0], L.pop()]
        
