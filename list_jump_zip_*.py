def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(3))


##递推函数


def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1  # n只起到决定决定循环次数的作用
    return s  # why the result will be different if the place if return change


print(power(5))


def greet(name='world'):
    print('hello', name)


print(greet())
print(greet('bob'))


def fn(*args):
    print(args)


def mean(*num):  # * 号表示1-无尽个数
    if len(num) > 0:
        return sum(num) * 1.0 / len(num)
    else:
        return 0


print(mean(1, 3, 5))

L = (1, 4, 5)
SUM = 0
for x in L:
    SUM = SUM + x
print(SUM)

L = ['ada', 'lisa', 'bart', 'paul']
print(L[::2])
# L[::] 历遍   L[::2] loop and jump when every two objects

M = list(range(0, 101))
print(M)
print(M[1:10])
print(M[::3])  # jump when every three objects
print(M[:50:5])  # only for first 50 num and jump when every five objects
print(M[-10:])
print(M[-46::5])

'abc'.upper()

L = list(range(1, 101))
for i in L:
    if i % 7 == 0:  # i % 7==0  means remiander is 0
        print(i)

d = {'a', 'b', 'c'}
for key in d:
    print(key)
for i, key in enumerate(['a', 'b', 'c']):
    print(i, key)

L = ['a', 'b', 'c', 'd']
M = [1, 2, 3, 4]
S = zip(M, L)
# zip object when need to be print out --- use list(S)
# zip like stapler


array = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = list(zip(*array))
print(transposed)

b = ["red", "green", "blue"]
f = ["strawberry", "kiwi", "blueberry"]

# simply think that zip is transpose the list
print(dict(zip(b, f)))

# transfer two list to dict  ---think it like transpose

person= collections.namedtuple('Person','name age height')
jane = person('Jane',25,1.75)
print(jane)

a=jane._asdict()
print(a)


for key, value in a.items():
    print(key + ':' ,value)

for field, value in zip(jane._fields, jane):
    print(field,'->', value)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(list(x))

for field, value in zip(a, b):
    print(field, 'marrys', value)
