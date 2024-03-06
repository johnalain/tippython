import pandas as pd
import sqlite3
data=pd.read_csv('bmi.csv',sep='\t')
con = sqlite3.connect('gta.db')

gta_data=pd.read_sql('select * from gta',con)
print(gta_data)