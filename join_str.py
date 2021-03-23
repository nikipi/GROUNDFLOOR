str='-'
seq=('I','will','love','you')
print(str.join(seq))

b=('I','am','angry')
c="!"
f=c.join(b)
print(f)

mark="~"

words=['I','am','so','free']

print(mark.join(words))

n = 2
s = "Programming"

print(s * n)

string = 'Hello There'
print (
    (s+' ')*2
)



def get_str_concat(*args):
    _str = ''
    firstLine = True
    for idx,arg in enumerate(args):
        if idx == 0:
            _str += arg
            forstLine  = False
            continue
        _str = _str + '_' + arg
    return _str

print(get_str_concat('qww','ss','qwe'))





--------------want to remove ''from the list
print('({})'.format(', '.join(("coin", "ensuite", "none"))))
