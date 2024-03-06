import pandas as pd



column = ['Michel','rita','josephine']
titled_columns = {'name':column,
                 'weight':[1.67,1.9,0.25],
                 'height':[54,100,1]}
#insert above list in dataframe
data = pd.DataFrame(titled_columns)#initialize dataframe
select_column = data['weight'][1]#[1]u can add index to select rita
select_row = data.iloc[1]['weight']#we can add ['weight'] if intersted in weight only

bmi = []
for i in range(len(data)):
    bmi_score = data['weight'][i]/(data['height'][i]**2)
    bmi.append(bmi_score)
data['bmi']= bmi#this loop add column of bmi
data.to_csv('bmi.txt', index=False ,sep='\t')#create and save data inside it
#sep=\t add tab seperator btween columns
#we can change the extension of bmi to .txt
#https://youtu.be/zN2Hua6oII0?list=PLlvFEn0NKwXKsfAM-mXulCXOtGvDKQs81&t=475




#https://youtu.be/zN2Hua6oII0?list=PLlvFEn0NKwXKsfAM-mXulCXOtGvDKQs81&t=278

print(data)


