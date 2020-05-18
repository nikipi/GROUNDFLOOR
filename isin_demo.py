keep_judges=list(df['authorship'].value_counts().index)[:11]
df=df[df['authorship'].isin(keep_judges)]
df['authorship'].value_counts()