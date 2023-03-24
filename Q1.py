##level 0
import datetime

def make_ticket(Id, day, month, hour, minute):
    ''' using a dispatch funtion we return every value that we recived according to indexing, then we return the dispatch'''
    def dispatch(i):
        if i == 0:return Id
        elif i == 1: return day
        elif i == 2: return month
        elif i == 3: return hour
        elif i == 4: return minute
    return dispatch

##level 1
def flight(t):
    '''to return the flight address ''' 
    return t(0)
def month(t):
    ''' to return the month  '''
    return t(2)
def date(t):
    ''' to return the date in a a oragnaized way'''
    def days(i):
        months = ['JAN', 'FEB','MAR', 'APR', 'MAY', 'JUNE',
                  'JULY','AUG','SEPT','OCT', 'NOV','DEC']
        return months[i-1]
    if t(2) == 2 and t(1) > 29:
        return 'Febraury has up to 29 days!'
    
    if t(1) >=10 and t(1) < 31 and t(2) > 0 and t(2) < 13:
        return '{0}{1}'.format(t(1), days(t(2)))
    if t(1) < 10:
        return '0{0}{1}'.format(t(1), days(t(2)))

def day(t):
    '''to return the day  ''' 

    return t(1)
def hour(t):
    '''to return the flight hour ''' 
    return t(3)

def minute(t):
    ''' to return the minute'''
    return t(4)

##level 2
def print_ticket_info(t, msg = 'flight date hh:mm'):
    '''here using an empty string then adding according if the hour is bigger than 10 or not'''
    thehour = ''
    if hour(t) >= 10: thehour+=str(hour(t))+':'
    else: thehour += '0{0}:'.format(hour(t)) 
    if minute(t) >= 10 : thehour+=str(minute(t)) 
    else:thehour += '0{0}'.format(minute(t))
    if msg == 'flight hh:mm':
        return flight(t)+" " + thehour
    elif msg == 'date hh:mm':
        return date(t)+" " + thehour
    elif msg == 'hh:mm':
        return thehour
    return flight(t) + " "  + date(t) + " "+ thehour


def time_diffrence(t1,t2):
    '''calculate the hours diffrence between the two instances then add the diffrence of minutes'''
    hours = hour(t1)- hour(t2)
    hours = hours * 60
    hours = hours + minute(t1) - minute(t2)
    return (lambda x : x if x > 0 else -1 * x) (hours)


def time_correction(t, minutes):
    ''' we get the current date and time then Add the number of minutes to the current datetime
        then we  extract the corrected date and time from the corrected datetime and then return a make tickect instance
    '''
    current_date = datetime.date(year=2020, month=month(t), day=day(t))
    current_time = datetime.time(hour=hour(t), minute=minute(t))
    current_datetime = datetime.datetime.combine(current_date, current_time)
    corrected_datetime = current_datetime + datetime.timedelta(minutes=minutes)
    corrected_date = corrected_datetime.date()
    corrected_time = corrected_datetime.time()
    return make_ticket(flight(t), corrected_date.day, corrected_date.month, corrected_time.hour, corrected_time.minute)             
t2 = make_ticket('TK0785', 8, 1, 10, 55)
    
t1 = make_ticket('F0545', 8, 1, 7, 40)
