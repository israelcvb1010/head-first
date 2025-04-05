def sanitize(time_strig):
    if '-' in time_strig:
        splitter = '-'
    elif ':' in time_strig:
        splitter = ':'
    else:
        return time_strig
    mins, secs = time_strig.split(splitter)
    return (mins + '.' + secs)

 
class AthleteList(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return sorted(set([sanitize(time) for time in self]))[0:3]
    

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return AthleteList(templ.pop(0), templ.pop(0), templ)
    except IOError as ioerr:
        print(f'File error: {ioerr}')
        return None

james = get_coach_data('james.txt')
print(f"{james.name}'s fastest times are: {james.top3()}")

julie = get_coach_data('julie.txt')
print(f"{julie.name}'s fastest times are: {julie.top3()}")

mikey = get_coach_data('mikey.txt')
print(f"{mikey.name}'s fastest times are: {mikey.top3()}")

sarah = get_coach_data('sarah.txt')
print(f"{sarah.name}'s fastest times are: {sarah.top3()}")