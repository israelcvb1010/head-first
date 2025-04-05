def sanitize(time_strig):
    if '-' in time_strig:
        splitter = '-'
    elif ':' in time_strig:
        splitter = ':'
    else:
        return time_strig
    mins, secs = time_strig.split(splitter)
    return (mins + '.' + secs)

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return {
            'Name': templ.pop(0),
            'DOB': templ.pop(0),
            'Times': str(sorted(set([sanitize(time) for time in templ]))[0:3]),
        }
    except IOError as ioerr:
        print(f'File error: {ioerr}')
        return None

james = get_coach_data('james.txt')
print(f"{james['Name']}'s fastest times are: {james['Times']}")

julie = get_coach_data('julie.txt')
print(f"{julie['Name']}'s fastest times are: {julie['Times']}")

mikey = get_coach_data('mikey.txt')
print(f"{mikey['Name']}'s fastest times are: {mikey['Times']}")

sarah = get_coach_data('sarah.txt')
print(f"{sarah['Name']}'s fastest times are: {sarah['Times']}")