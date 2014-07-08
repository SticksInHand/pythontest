def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif  ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins,secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('file error:' + str(ioerr))
        return(None)


james = get_coach_data("james.txt")
sarah = get_coach_data("sarah.txt")
julie = get_coach_data("julie.txt")
mikey = get_coach_data("mikey.txt")

clean_sarah = [sanitize(each_t) for each_t in sarah]
clean_julie = [sanitize(each_t) for each_t in julie]
clean_mikey = [sanitize(each_t) for each_t in mikey]
clean_james = [sanitize(each_t) for each_t in james]

distances_sarah = set(clean_sarah)
distances_julie = set(clean_julie)
distances_mikey = set(clean_mikey)
distances_james = set(clean_james)

print(sorted(distances_sarah)[0:3])
print(sorted(distances_julie)[0:3])
print (sorted(distances_mikey)[0:3])
print (sorted(distances_james)[0:3])

sarah2 = get_coach_data('sarah2.txt')
# (sarah_name,sarah_dob) = sarah2.pop(0),sarah2.pop(0)
# print(sarah_name + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah2]))[0:3]))
sarah_data = {}
sarah_data['Name'] = sarah2.pop(0)
sarah_data['DOB'] = sarah2.pop(0)
sarah_data['Times'] = sarah2

print (sarah_data['Name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))























