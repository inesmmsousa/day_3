'''
Created on 06/02/2018

@author: Utilizador
'''


def is_number(valor):
    '''
    param: any value
    return: int if value is integer
    '''
    
    try:
        return int(valor)
    except:
        return None
    
    
def vect_float(valor):
    '''
    param: any value
    return: float
    '''
    
    try:
        return float(valor)
    except:
        return None