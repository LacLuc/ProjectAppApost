from time import sleep
import datetime 

def GetID():
  sleep(1)
  now = datetime.datetime.now()
  return f'{now.year}{now.month}{now.day}{now.hour - 3}{now.minute}{now.second}'