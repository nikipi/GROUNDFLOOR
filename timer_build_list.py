from timeit import Timer


def test1():
 for i in range(1,11):
    l=list(range(i))


def test2():
 l=[]
 for i in range(1,11):
     l.append(i)


timer1=Timer("test1()","from __main__ import test1")
print('range:',timer1.timeit(1000))

timer2=Timer("test2()","from __main__ import test2")
print('append',timer2.timeit(1000))




