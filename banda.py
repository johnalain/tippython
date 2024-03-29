import pandas as pd
import numpy as np
mydata = ['boat','bike','car','track']
myseries1 = pd.Series(mydata)
print(myseries1)
print('----------')

mydata = [1,195,300,5]
myserie2 = pd.Series(mydata)
print(myserie2)
print('----------')

mydfdata = [('boat',1),('bike', 195),('car',300),('track',5)]
mydf = pd.DataFrame(mydfdata)
print(mydf)#output:
#        0    1
# 0   boat    1
# 1   bike  195
# 2    car  300
# 3  track    5

mydfdata = [('boat',1),('bike', 195),('car',300),('track',5)]
mydf = pd.DataFrame(mydfdata ,columns=['things','count'])
print(mydf)#output:
#   things  count
# 0   boat      1
# 1   bike    195
# 2    car    300
# 3  track      5
print(mydf['things'])#output:
# 0     boat
# 1     bike
# 2      car
# 3    track
# Name: things, dtype: object

print(mydf['count'])#output:
# 0      1
# 1    195
# 2    300
# 3      5
# Name: count, dtype: int64

print(mydf.dtypes)#output:
# things    object
# count      int64
# dtype: object

#READING IN DATA
df = pd.read_csv('//Users//michelkadi//Desktop//Book1invoice1.csv')
print(df.head())#read five columns from file
print(df)
print('=============== ')
print(df.dtypes)
print('=============== ')
print(df.describe)
print(df['2211'])#print one column according to its name
#https://youtu.be/_Eb0utIRdkw?list=PLlvFEn0NKwXK-ClUmxWk1zUmF5hRCXKYV&t=887
print('=============== ')
print(df.loc[4])
print('===============')
print(df.columns)
print('===============')
df = df[['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', '45358']]
print(df)
print('===============')
print(df.shape)
print('===============')
print(df[' unamed:0'])>1000000
#https://youtu.be/_Eb0utIRdkw?list=PLlvFEn0NKwXK-ClUmxWk1zUmF5hRCXKYV&t=1317

