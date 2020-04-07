for i in range(1,5):
    print(' '*(4-i),end="")
    print('*'*(2*i-1),end="") #line 132,133没怎么看懂 print里也没用到J啊
    print()
for i in range(3,0,-1):
    print(' '*(4-i),end="")
    for j in range(1,2*i):
        print('*',end="")
    print()





