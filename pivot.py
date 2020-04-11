import pandas as pd

data=pd.read_csv('/Users/apple/Desktop/macrodata.csv')

print(data.head())

'''

data=data.loc[:,['realgdp','infl','unemp']]
print(data.head())
'''

periods=pd.PeriodIndex(year=data.year,quarter=data.quarter,name='date')

columns=pd.Index(['realgdp','infl','unemp'],name='item')

data=data.reindex(columns=columns)

data.index=periods.to_timestamp('D','end')

print(data.head())


##########
#pivot####
##########

df=pd.DataFrame({'key':['foo','bar','baz'],
                 'A':[1,2,3],
                 'B':[4,5,6],
                 'C':[7,8,9]})

print(df)

melted=pd.melt(df,['key'])
print(melted)

reshaped=melted.pivot('key','variable','value')  # key-raw varibale-columns value-entry
print(reshaped)