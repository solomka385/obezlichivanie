import pandas as pd
from get_group import *
df_name = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/name_grouped.xlsx')
df_fam = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/fam_grouped.xlsx')
df_otch = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/otch_grouped.xlsx') 

df_name_new = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/name_new.xlsx')
df_fam_new  = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/fam_new.xlsx')
df_otch_new  = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/otch_new.xlsx') 

def namee(name):
    s = df_name[df_name['#Name'] == name.upper()]
    name_popularity = 0
    new_name = ''
    name_popularity = int(s.iloc[0]['POPULARITY']) 
    gender = int(s.iloc[0]['GENDER']) 
    kod_populary_name = name_gr(name_popularity)
    new_name = df_name[(df_name['GROUP'] == kod_populary_name) & (df_name['GENDER'] == gender)].sample().iloc[0]['#Name'] 
    return new_name.capitalize()

def fam(name):
    s = df_fam[df_fam['#Формат: Фамилия'] == name.upper()]
    fam_popularity = 0
    new_fam = ''
    fam_popularity = int(s.iloc[0]['POPULARITY']) 
    gender = int(s.iloc[0]['GENDER']) 
    kod_populary_fam = fam_gr(fam_popularity)
    new_fam = df_fam[(df_fam['GROUP'] == kod_populary_fam) & (df_fam['GENDER'] == gender)].sample().iloc[0]['#Формат: Фамилия'] 
    return new_fam.capitalize()

def otch(name):
    s = df_otch[df_otch['#Отчество'] == name.upper()]
    otch_popularity = 0
    new_otch = ''
    otch_popularity = int(s.iloc[0]['POPULARITY']) 
    gender = int(s.iloc[0]['GENDER']) 
    kod_populary_otch = otch_gr(otch_popularity)
    new_otch = df_otch[(df_otch['GROUP'] == kod_populary_otch) & (df_otch['GENDER'] == gender)].sample().iloc[0]['#Отчество'] 
    return new_otch.capitalize()


