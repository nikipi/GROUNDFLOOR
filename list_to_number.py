#给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

a=[]
for i in range(3):
    numo=input('please enter a number:')
    a.append(numo)

c="".join(a)
print(c)
c=sorted(c,reverse=True)
c="".join(c)
print(c)
