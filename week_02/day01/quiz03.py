# Split


def extract_first_last_name(names):
    fname = []
    l_name = []
    for name in names:
        split_name = name.split(' ')
        fname.append(split_name[0])
        l_name.append(split_name[-1])

    return fname, l_name

names = ['Tom Cruise', 'Eden Hazard', 'Paul Pogba', 'Harry Potter']
print(extract_first_last_name(names))