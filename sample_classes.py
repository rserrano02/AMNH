class simple_arithmetic : 
    '''This object takes two arguments at initialization.
    There are fourt methods that will return simple simple arithmetic operations'''
    def __init__(self, arg1, arg2) :
        self.arg1 = arg1
        self.arg2 = arg2
    def add (self) :
        return self.arg1 + self.arg2 
    def sub (self) :
        return self.arg1 - self.arg2
    def div (self) :
        return self.arg1 / self.arg2
    def mul (self): 
        return self.arg1 * self.arg2
