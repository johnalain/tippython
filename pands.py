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
select_column = data['weight'][1],[2],[3]
print(select_column)
# output (56, [2], [3])


#output
# 0    72
# 1    56
# 2    62
# 3    10

