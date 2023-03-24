def make_temperature(temp, sign):
    ''' using a dispatch function that includes getvalue wich return the value according
to the message was sent, and a  setvalue function that gives the argument was sent a new value
and the convert function is responsible of converting the degree, then we return the dispatch functuion'''
    def dispatch(msg1):
        def getvalue(msg2):
            if msg2 == 'degrees':
                return temp
            elif msg2 == 'unit':
                return sign
            else: return 'Unkown'
        def setvalue(msg2, val):
            nonlocal temp
            nonlocal sign
            if msg2 == 'degrees':
                temp = val
            elif msg2 == 'unit':
                 sign = val
            else: return 'Unkown'
        def convert(func, Newsign):
            nonlocal temp
            nonlocal sign
            temp = func(temp)
            sign = Newsign
        if msg1 == 'get_value':
            return getvalue
        elif msg1 == 'set_value':
            return setvalue
        elif msg1 == 'str':
            return '{0:.2f} {1}'.format(temp, sign)
        elif msg1 == 'convert':
            return convert
    return dispatch


t = make_temperature(25, 'C')
