__author__ = 'M.Jin'
class Athlete(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])


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

vera = Athlete('veravi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22','1-21','2:22'])
print(vera.top3())
