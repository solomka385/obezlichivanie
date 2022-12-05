
import psycopg2
import pandas as pd
from func_for_physical import *

from email_generator import *
print(str(None))
cdi_stress=psycopg2.connect(database='education',user='cdi_stress', password='cdi',host='10.0.72.12', port='5432')
df = pd.read_sql(("SELECT * from "+' physical_party '+" limit 25;"),cdi_stress)
print(df[['name','surname','patronymic','inn','snils','id_party','birthdate']])
