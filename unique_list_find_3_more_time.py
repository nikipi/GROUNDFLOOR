#查找所有至少连续出现三次的数字

import pandas as pd

df=pd.DataFrame({'id':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],

                 'num':[1,2,1,1,1,2,3,3,3,3,4,6,7,8,9]})

def unique(listA):
    # return list(set(listA))
    return sorted(set(listA), key=listA.index)
a=[]
for i in range(len(df)-2):
    if df['num'][i]==df['num'][i+1]==df['num'][i+2]:
        a.append(df['num'][i])

        c=unique(a)
        print(c)


num=[1,2,1,1,1,2,3,3,3,3,4,6,7,8,9]
print(unique(num))