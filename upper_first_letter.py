def format_name(s):

    return s.capitalize()

S=list (map(format_name, ['adam', 'LISA', 'barT']))

print(S)


my_name = 'Yulu Pi'

def upper_first(name):
    first_space= name.find(' ')
    return name[0:first_space].upper()+name[first_space:]

print(upper_first(my_name))





