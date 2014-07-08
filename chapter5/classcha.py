class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])

    def add_time(self,time):
        self.times.append(time)

    def add_times(self,timelist):
        self.times.extend(timelist)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        temp1 = data.strip().split(',')
        return Athlete(temp1.pop(0),temp1.pop(0),temp1)
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return (None)
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif  ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.split(splitter)
    return (mins + '.' + secs)

james = get_coach_data('james2.txt')

print (james.name + "'s fastest times are: " + str(james.top3()))