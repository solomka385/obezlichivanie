import pandas as pd
from get_group import *
import openpyxl as ox
import datetime
from random import *
df_name = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/name_grouped.xlsx')
df_fam = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/fam_grouped.xlsx')
df_otch = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/otch_grouped.xlsx') 

#df_new = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/new.xlsx')
path = 'C://Users/alex1/Desktop/project_for_danniy/new.xlsx'

def bithday(date):
    if len(str(date)) > 6:
        s = str(date).split('-')
        
        d31 = ['01','03','05','07','08','10','12']
        d30 = ['04','06','09','11']
        d28 = ['02']
        print(s)
        if s[1] in d31:
            date = datetime.datetime.strptime((s[0] +'-'+s[1]+'-'+ str(randint(1,31))),'%Y-%m-%d')
            
        if s[1] in d30:
            date = datetime.datetime.strptime((s[0] +'-'+s[1]+'-'+ str(randint(1,30))),'%Y-%m-%d')
        if s[1] in d28:
            date = datetime.datetime.strptime((s[0] +'-'+s[1]+'-'+ str(randint(1,28))),'%Y-%m-%d')
        return date


def name(namee):
    
    
    
    try:
        s = df_name[df_name['#Name'] == str(namee[2]).upper()]
        name_popularity = 0
        new_name = ''
        name_popularity = int(s.iloc[0]['POPULARITY']) 
        gender = int(s.iloc[0]['GENDER']) 
        
        kod_populary_name = name_gr(name_popularity)
        new_name = df_name[(df_name['GROUP'] == kod_populary_name) & (df_name['GENDER'] == gender)].sample().iloc[0]['#Name'] 
        namee[3] = new_name.capitalize()
        
        return namee
    except:
        
       # sjj = {'name': str(namee).upper(), 'id_party':idd}
        
        #df_new.append(sjj,ignore_index=True)
        
        namee[3] = df_name[(df_name['GROUP'] == 1)].sample().iloc[0]['#Name'].capitalize()
        
        return namee
        


def surname(name):
    
    try:
        s = df_fam[df_fam['#Формат: Фамилия'] == str(name).upper()]
        fam_popularity = 0
        new_fam = ''
        fam_popularity = int(s.iloc[0]['POPULARITY']) 
        gender = int(s.iloc[0]['GENDER']) 
        
        kod_populary_fam = fam_gr(fam_popularity)
        new_fam = df_fam[(df_fam['GROUP'] == kod_populary_fam) & (df_fam['GENDER'] == gender)].sample().iloc[0]['#Формат: Фамилия'] 
        name[2] = new_fam.capitalize()
        return name
    except:
        
        name[2] =  df_fam[(df_fam['GROUP'] == 1)].sample().iloc[0]['#Формат: Фамилия'].capitalize()
        return name
def patronymic(name):
    
    try:
        s = df_otch[df_otch['#Отчество'] == str(name).upper()]
        otch_popularity = 0
        new_otch = ''
        otch_popularity = int(s.iloc[0]['POPULARITY']) 
        gender = int(s.iloc[0]['GENDER']) 
        kod_populary_otch = otch_gr(otch_popularity)
        new_otch = df_otch[(df_otch['GROUP'] == kod_populary_otch) & (df_otch['GENDER'] == gender)].sample().iloc[0]['#Отчество'] 
        name[4] = new_otch.capitalize()
        return name
    except:
        name[4] = df_otch[(df_otch['GROUP'] == 1)].sample().iloc[0]['#Отчество'].capitalize()
        return name

def inn(chislo):
    
    if len(str(chislo)) == 12:
        inn = (str(chislo)[0:4] +  ''.join([choice(['1','2','3','4','5','6','7','8','9']) for x in range(6)]) )
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
        inn = (str(chislo)[0:4] +  ''.join([choice(['1','2','3','4','5','6','7','8','9']) for x in range(5)]) )
        inn_list = list(map(int,inn))
        last = 0
        mnoshiteli = [2,4,10,3,5,9,4,6,8]
        summ = 0
        for i in range(len(inn_list)):
            summ += inn_list[i]*mnoshiteli[i]
        last = str((summ %11)%10)
        inn += last
        return inn
    return 'None'

def snils(snils):
    
    if type(str(snils)) == 14:
        
        k = range(9, 0, -1)
        snils = (''.join([choice(['1','2','3','4','5','6','7','8','9']) for x in range(3)]) )
        snils += '-'
        snils +=  (''.join([choice(['1','2','3','4','5','6','7','8','9']) for x in range(3)]) )
        snils+='-'
        snils += (''.join([choice(['1','2','3','4','5','6','7','8','9']) for x in range(3)]) )
        pairs = zip(k, [int(x) for x in snils.replace('-', '').replace(' ', '')])
        csum = sum([k * v for k, v in pairs])
        while csum > 101:
            csum %= 101
        if csum in (100, 101):
            csum = 0
        snils += ' '
        snils += str(csum)
        return snils
    return snils
