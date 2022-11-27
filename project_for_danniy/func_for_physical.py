import psycopg2
import pandas as pd
df_name = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/name.xlsx')
df_fam = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/fam.xlsx')
df_otch = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/otch.xlsx') 

df_name_new = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/name_new.xlsx')
df_fam_new  = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/fam_new.xlsx')
df_otch_new  = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/otch_new.xlsx') 


"""
cdi_stress=psycopg2.connect(database="education",user="cdi_stress", password="cdi",host="10.0.72.12", port="5432")
df = pd.read_sql("SELECT * from address limit 10;",cdi_stress)
print(df)"""
#print(df_name)

def name(name):
    s = df_name[df_name['#Name'] == name]
    name_popularity = 0
    new_name = ''
    name_popularity = int(s.iloc[0]['POPULARITY']) 
    if name_popularity in range(0,1000): 
        new_name = df_name[(df_name['POPULARITY'] >= 0) & (df_name['POPULARITY'] <= 1000 )].sample().iloc[0]['#Name'] 
    elif name_popularity in range(0,10000): 
        new_name = df_name[(df_name['POPULARITY'] >= 0) & (df_name['POPULARITY'] <= 1000 )].sample().iloc[0]['#Name'] 
    elif name_popularity in range(0,25000): 
        new_name = df_name[(df_name['POPULARITY'] >= 0) & (df_name['POPULARITY'] <= 1000 )].sample().iloc[0]['#Name'] 
    elif name_popularity in range(0,50000): 
        new_name = df_name[(df_name['POPULARITY'] >= 0) & (df_name['POPULARITY'] <= 1000 )].sample().iloc[0]['#Name'] 
    elif name_popularity in range(0,75000): 
        new_name = df_name[(df_name['POPULARITY'] >= 0) & (df_name['POPULARITY'] <= 1000 )].sample().iloc[0]['#Name'] 
    elif name_popularity in range(0,1000): 
        new_name = df_name[(df_name['POPULARITY'] >= 0) & (df_name['POPULARITY'] <= 1000 )].sample().iloc[0]['#Name'] 
    elif name_popularity in range(0,1000): 
        new_name = df_name[(df_name['POPULARITY'] >= 0) & (df_name['POPULARITY'] <= 1000 )].sample().iloc[0]['#Name'] 
    
    return new_name

def fam(name):
    s = df_fam[df_fam['#Формат: Фамилия'] == name]
    fam_popularity = 0
    new_fam = ''
    fam_popularity = int(s.iloc[0]['POPULARITY']) 
    if fam_popularity in range(0,1000): 
        new_fam = df_fam[(df_fam['POPULARITY'] >= 0) & (df_fam['POPULARITY'] <= 1000 )].sample().iloc[0]['#Формат: Фамилия'] 
    return new_fam

def otch(name):
    s = df_otch[df_otch['#Отчество'] == name]
    otch_popularity = 0
    new_otch = ''
    otch_popularity = int(s.iloc[0]['POPULARITY']) 
    if otch_popularity in range(0,1000): 
        new_otch = df_otch[(df_otch['POPULARITY'] >= 0) & (df_otch['POPULARITY'] <= 1000 )].sample().iloc[0]['#Отчество'] 
    return new_otch





#cdi_stress.close()