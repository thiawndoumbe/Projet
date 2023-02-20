import pandas as pd
import numpy as np
df=pd.read_excel("nfl_players.xlsx")
df.head()
df.columns

df=df.drop(['web-scraper-order', 'web-scraper-start-url'],axis=1)
df.head()
df.dtypes
df.shape
df.isnull().sum()
Numerical_columns = []
for var in df.columns :
    if var == 'Player' or var=='Pass Yds':
        continue
    else: 
        Numerical_columns.append(var)
Numerical_columns

#rechercher s'il y'a des 0 
zero_count=[]
for col in Numerical_columns:
    count=0
    for i in df[col]:
        if i==0:
            count+= 1
    zero_count.append(count)            
            
zero_count
df['40+']=df['40+'].mean()
    
    
zero_count
df[["first_name_Players","second_name_Players"]]=df.Player.str.split(" ",n=1, expand=True)
df.head()
df=df.drop(["Player"],axis=1)
df.head()
df.columns
columns=(['first_name_Players','second_name_Players','Pass Yds', 'Yds/Att', 'Att', 'Cmp', 'Cmp %', 'COL_TD', 'INT', 'Rate',
       '1st', '1st%', '20+', '40+', 'Lng', 'Sck', 'SckY'
       ])
df=df[columns]
df.head()
