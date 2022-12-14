import pandas as pd
from get_group import *
import openpyxl as ox
import datetime
from random import *
from old_to_new import *

df_name = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/name_grouped.xlsx')
df_fam = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/fam_grouped.xlsx')
df_otch = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/otch_grouped.xlsx') 

df_new_name = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/name_new.xlsx')
df_new_surname = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/surname_new.xlsx')
df_new_otch = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/otch_new.xlsx')
df_new_inn= pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/inn_new.xlsx')
df_new_snils = pd.read_excel('C://Users/alex1/Desktop/project_for_danniy/snils_new.xlsx')



def bithday(date):
    
    if len(str(date[5])) > 6:
        s = str(date[5]).split('-')
        
        d31 = ['01','03','05','07','08','10','12']
        d30 = ['04','06','09','11']
        d28 = ['02']
        
        if s[1] in d31:
            date[5] = datetime.datetime.strptime((s[0] +'-'+s[1]+'-'+ str(randint(1,31))),'%Y-%m-%d')
            
        if s[1] in d30:
            date[5] = datetime.datetime.strptime((s[0] +'-'+s[1]+'-'+ str(randint(1,30))),'%Y-%m-%d')
        if s[1] in d28:
            date[5] = datetime.datetime.strptime((s[0] +'-'+s[1]+'-'+ str(randint(1,28))),'%Y-%m-%d')
        
        return date


def name(namee):
    
    try:
        
        s = df_new_name[df_new_name['name'] == str((namee[3]))]
        
        namee[3] = s.iloc[0]['name_new']
        print(s)
        return namee
    except:
        name_ = namee[3]
        
        try:
            
            s = df_name[df_name['#Name'] == str(namee[3]).upper()]
            name_popularity = 0
            new_name = ''
            name_popularity = int(s.iloc[0]['POPULARITY']) 
            gender = int(s.iloc[0]['GENDER'])
            
            kod_populary_name = name_gr(name_popularity)
            new_name = df_name[(df_name['GROUP'] == kod_populary_name) & (df_name['GENDER'] == gender)].sample().iloc[0]['#Name'] 
            namee[3] = new_name.capitalize()
            
            id_exist(name_,'C://Users/alex1/Desktop/project_for_danniy/name_new.xlsx',namee[3])
            return namee
        except:
            
       
            
            namee[3] = df_name[(df_name['GROUP'] == 1)].sample().iloc[0]['#Name'].capitalize()
            
            id_exist(name_,'C://Users/alex1/Desktop/project_for_danniy/name_new.xlsx',namee[3])
            return namee
            


def surname(name):
    try:
        s = df_new_surname[df_new_surname['surname'] == str(name[2])]
        name[2] = s.iloc[0]['surname_new']
        return name
    except:
        name_ = name[2]
        
        try:
            s = df_fam[df_fam['#Формат: Фамилия'] == str(name[2]).upper()]
            fam_popularity = 0
            new_fam = ''
            fam_popularity = int(s.iloc[0]['POPULARITY']) 
            gender = int(s.iloc[0]['GENDER']) 
            
            kod_populary_fam = fam_gr(fam_popularity)
            new_fam = df_fam[(df_fam['GROUP'] == kod_populary_fam) & (df_fam['GENDER'] == gender)].sample().iloc[0]['#Формат: Фамилия'] 
            name[2] = new_fam.capitalize()
            id_exist(name_,'C://Users/alex1/Desktop/project_for_danniy/surname_new.xlsx',name[2])
            return name
        except:
            
            name[2] =  df_fam[(df_fam['GROUP'] == 1)].sample().iloc[0]['#Формат: Фамилия'].capitalize()
            id_exist(name_,'C://Users/alex1/Desktop/project_for_danniy/surname_new.xlsx',name[2])
            return name
def patronymic(name):
    
    try:
        s = df_new_otch[df_new_otch['patronymic'] == (name[4])]
        name[4] = s.iloc[0]['patronymic_new']
        return name
    except:
        name_ = name[4]
    
        try:
            s = df_otch[df_otch['#Отчество'] == str(name[4]).upper()]
            otch_popularity = 0
            new_otch = ''
            otch_popularity = int(s.iloc[0]['POPULARITY']) 
            gender = int(s.iloc[0]['GENDER']) 
            kod_populary_otch = otch_gr(otch_popularity)
            new_otch = df_otch[(df_otch['GROUP'] == kod_populary_otch) & (df_otch['GENDER'] == gender)].sample().iloc[0]['#Отчество'] 
            name[4] = new_otch.capitalize()
            id_exist(name_,'C://Users/alex1/Desktop/project_for_danniy/otch_new.xlsx',name[4])
            return name
        except:
            name[4] = df_otch[(df_otch['GROUP'] == 1)].sample().iloc[0]['#Отчество'].capitalize()
            id_exist(name_,'C://Users/alex1/Desktop/project_for_danniy/octh_new.xlsx',name[4])
            return name

def inn(chislo):
    try:
        s = df_new_inn[df_new_inn['inn'] == str(chislo[1])]
        chislo[1] = s.iloc[0]['inn_new']
        return chislo
    except:
        name_ = chislo[1]
        
        if len(str(chislo[1])) == 12:
            
            inn = (str(chislo[1])[0:4] +  ''.join([choice(['1','2','3','4','5','6','7','8','9']) for x in range(6)]) )
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
            chislo[1] = inn
            
            id_exist(name_,'C://Users/alex1/Desktop/project_for_danniy/inn_new.xlsx',chislo[1])
            return chislo
        
        elif len(str(chislo[1])) == 10:
            inn = (str(chislo[1])[0:4] +  ''.join([choice(['1','2','3','4','5','6','7','8','9']) for x in range(5)]) )
            inn_list = list(map(int,inn))
            last = 0
            mnoshiteli = [2,4,10,3,5,9,4,6,8]
            summ = 0
            for i in range(len(inn_list)):
                summ += inn_list[i]*mnoshiteli[i]
            last = str((summ %11)%10)
            inn += last
            chislo[1] = inn
            id_exist(name_,'C://Users/alex1/Desktop/project_for_danniy/inn_new.xlsx',chislo[1])
            return chislo
            
        chislo[1] = 'None'
        id_exist(name_,'C://Users/alex1/Desktop/project_for_danniy/inn_new.xlsx',chislo[1])
        return chislo

def snils(snilss):
    try:
        s = df_new_snils[df_new_snils['snils'] == str(snilss[6])]
        snilss[6] = s.iloc[0]['snils_new']
        
        return snilss
    except:
        name_ = snilss[6]
        
        if type(str(snilss)) == 14:
            
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
            snilss[6] = snils
            id_exist(name_,'C://Users/alex1/Desktop/project_for_danniy/inn_new.xlsx',snilss[6])
            
            return snilss
        id_exist(name_,'C://Users/alex1/Desktop/project_for_danniy/inn_new.xlsx',snilss[6])
        
        return snilss
