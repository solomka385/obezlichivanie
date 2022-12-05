from random import *

def nomer(tele,id):
    print(id)
    tele = ( ''.join([choice(['1','2','3','4','5','6','7','8','9']) for x in range(len(str(tele)))]) )
    return tele
