import pandas as pd

df=pd.DataFrame({'id':[1,2,3,4,5],
                'score':[3.5,5,6,3.5,7]})

print(df)

df1=df.sort_values('score')
print(df1)

m=df['score'].unique()
print(m)

df1['rank']=df1['score'].rank(method='dense')   # dense -- the same score has the same rank
print(df1)


