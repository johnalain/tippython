import pandas as pd 
column = ['michel','rita','josephine','amal']
# titled_column = {'name':column}
# data = pd.DataFrame(titled_column)

# print (data)
#output:without titled_column
# 0     michel
# 1       rita
# 2  josephine
# 3       amal

# when we add titled_column
#         name
# 0     michel
# 1       rita
# 2  josephine
# 3       amal

titled_columns = {'name':column,
                  'height':[176,120,124,110],
                  'weight':[72,56,62,10]}
# data = pd.DataFrame(titled_columns)
# print(data)

#output:        name  height  weight
# 0     michel     176      72
# 1       rita     120      56
# 2  josephine     124      62
# 3       amal     110      10
#https://youtu.be/zN2Hua6oII0?list=PLlvFEn0NKwXKsfAM-mXulCXOtGvDKQs81&t=227
data = pd.DataFrame(titled_columns)
# select_column = data['weight']
# select_column = data['weight'][1],[2],[3]
# select_row = data.iloc [1]#output (56, [2], [3])
select_column = data['weight'][1]
select_row = data.iloc [1]['weight']
print(select_row)#select output:name      rita
#height     120
#weight      56
# output (56, [2], [3])


#output
# 0    72
# 1    56
# 2    62
# 3    10
bmi = []
for i in range(len(data)):
    bmi_score = data['weight'][i]/(data ['height'][i]**2)
    bmi.append(bmi_score)
    data [bmi] = bmi_score
    data.to_csv('bmi.csv',sep = '/')
print (data)
#output:  name  height  weight  0.002324  0.003889  0.004032  0.000826
# 0     michel     176      72  0.000826  0.000826  0.000826  0.000826
# 1       rita     120      56  0.000826  0.000826  0.000826  0.000826
# 2  josephine     124      62  0.000826  0.000826  0.000826  0.000826
# 3       amal     110      10  0.000826  0.000826  0.000826  0.000826
