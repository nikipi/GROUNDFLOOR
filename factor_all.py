M = []
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
          M.append(i)

print(M)

from pip._vendor.distlib.compat import raw_input

L=[]
a=int(raw_input("please enter a number:"))
if a==1:
    print(a)
else:
    for i in M[:]:
        if a%i==0:
            L.append(i)
            a/=i
print(L)

