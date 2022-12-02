import psycopg2
import pandas as pd
from address_func import *

cdi_stress=psycopg2.connect(database="education",user="cdi_stress", password="cdi",host="10.0.72.12", port="5432")
df = pd.read_sql("SELECT * from address limit 10;",cdi_stress)
print(df)
for index in range(len(df)):
    if df['postalcode'].loc[index] != None:
        df['street'].loc[index] = address(df['postalcode'].loc[index],df['street'].loc[index])




print(df)
cdi_stress.close()