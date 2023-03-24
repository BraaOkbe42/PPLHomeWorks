from copy import deepcopy
def make_traveler_trip(name, idd):
    '''
in make_traveler_trip, we first declared the function add_destination
that's responsible of adding dictianaries to our dictionary
and the function search_destination is responsible of showing all the relevant
according to the destination it reseaved, the function view is responsible of
showing either destinations or locations according to message was sent
print_trip is a function that returns a dispatch dictionary with two functions
hasMore and next , hasmore is responsible of checking if the dictionary that we
made a deep copy of that it has elements, next is  a funtion that shows you the next element
in the dictionary.
at last we return a dispatch dictionary that has all these functions !

 '''
    travelerName = name
    travelerId = idd
    travelersDict = dict()
    
    def add_destination(city, country, charge, symbol):
        travelersDict[city]={'location': country
                             , 'cost': charge,
                             'currency': symbol}
        

    def search_destination(dest):
        if dest not in travelersDict:
            print('destination not found!')
        else:
            print('{0}, {1}, {2} {3}'.format(dest, travelersDict[dest]['location'],
                                             travelersDict[dest]['cost'],
                                             travelersDict[dest]['currency']))
    def view(msg):
        if msg == 'destinations':
            for i in travelersDict:
                print(i, end=', ')
        if msg == 'locations':
            locations = set()
            for i in travelersDict.values():
                locations.add(i['location'])
            for _ in locations:
                print(_, end = " ")

    
    def print_trip():
        print(travelerName,travelerId)
        newdict = deepcopy(travelersDict)
        def next1():
            pop = newdict.popitem()
            search_destination(pop[0])
        def hasMore():
            return len(newdict)> 0
        return {'hasMore': hasMore, 'next': next1}
    def calculate_expenses(curr):
        def calc_charge(msg, val, msg2):
            exp = 0
            if msg2 == 'ILS':   
                if msg  == 'EUR':
                    exp += val * 3.69
                elif msg == 'ILS':
                    exp+=val
                elif msg == 'USD':
                    exp+=val * 3
            if msg2 == 'EUR':
                if msg  == 'EUR':
                    exp += val 
                elif msg == 'ILS':
                    exp+=val * 0.27
                elif msg == 'USD':
                    exp+=val * 0.94
            if msg2 == 'USD':
                if msg  == 'EUR':
                    exp += val * 1.06
                elif msg == 'ILS':
                    exp+=val * 0.29
                elif msg == 'USD':
                    exp+=val
            return exp        
        exp= 0
        for i in travelersDict.values():
            exp += calc_charge(i['currency'],int(i['cost']), curr)
        return exp

    
    def delete_destination(city):
        if city not in travelersDict:
            return 'Destination not found!'
        del travelersDict[city]
        
    return {'add_destination': add_destination, 'search_destination': search_destination,
            'delete_destination': delete_destination, 'calculate_expenses': calculate_expenses,
            'view':view, 'print_trip':print_trip}
    
##mt=make_traveler_trip('Shahar', 1)
##mt['add_destination']('Vondelpark', 'Amsterdam', '15', 'EUR')
##mt['add_destination']('ADAM Lookout', 'Amsterdam', '153', 'ILS')
##mt['add_destination']('Lauterbrunnen', 'Switzerland', '1000', 'ILS')
##mt['add_destination']('Greendelwald', 'Switzerland', '167', 'EUR')
##mt['add_destination']('Lake Como', 'Italy', '30', 'EUR')
