import datetime 

def horario():  
    now = datetime.datetime.now()   
    print(f'{dia(now)}-{hora(now)}')

def dia(now):
    dia = f'Data:{str(now.day).zfill(2)}/{str(now.month).zfill(2)}/{str(now.year).zfill(2)}'
    return dia

def hora(now):     
    hora = f'{str(now.hour).zfill(2)}:{str(now.minute).zfill(2)}:{str(now.second).zfill(2)}'
    return hora

