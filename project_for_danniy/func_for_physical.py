import pandas as pd
from get_group import *
import random
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

def inn(chislo):
    if len(str(chislo)) == 12:
        inn = (str(chislo)[0:4] +  ''.join([random.choice(['1','2','3','4','5','6','7','8','9']) for x in range(6)]) )
        inn_list = list(map(int,inn))
        last_1 = 0
        last_2 = 0
        mnoshiteli_1 = [7,2,4,10,3,5,9,4,6,8]
        mnoshiteli_2 = [3,2,4,10,3,5,9,4,6,8]
        summ_1 = 0
        summ_2 = 0
        for i in range(len(inn_list)):
            summ_1 += inn_list[i]*mnoshiteli_1[i]
            summ_2 += inn_list[i]*mnoshiteli_2[i]
        last_1 = str((summ_1% 11)%10)
        last_2 = str((summ_2% 11)%10)
        inn += last_1 
        inn += last_2
        return inn
        
    elif len(str(chislo)) == 10:
        inn = (str(chislo)[0:4] +  ''.join([random.choice(['1','2','3','4','5','6','7','8','9']) for x in range(5)]) )
        inn_list = list(map(int,inn))
        last = 0
        mnoshiteli = [2,4,10,3,5,9,4,6,8]
        summ = 0
        for i in range(len(inn_list)):
            summ += inn_list[i]*mnoshiteli[i]
        last = str((summ %11)%10)
        inn += last
        return inn

def snils(snils):
    if type(snils) != None:
        k = range(9, 0, -1)
        snils = (''.join([random.choice(['1','2','3','4','5','6','7','8','9']) for x in range(3)]) )
        snils += '-'
        snils +=  (''.join([random.choice(['1','2','3','4','5','6','7','8','9']) for x in range(3)]) )
        snils+='-'
        snils += (''.join([random.choice(['1','2','3','4','5','6','7','8','9']) for x in range(3)]) )
        pairs = zip(k, [int(x) for x in snils.replace('-', '').replace(' ', '')])
        csum = sum([k * v for k, v in pairs])
        while csum > 101:
            csum %= 101
        if csum in (100, 101):
            csum = 0
        snils += '-'
        snils += str(csum)
        return snils

