import sys
import src.services.Hour as Hour
import random
from rich.progress import track
from time import sleep
import datetime 

def print_version(): 
    #hr()   
    x = random.randint(1, 20) 
    if x == 2:        
        print(print_random_python_version(), sys.api_version)
        print(sys.getrecursionlimit)
        print(sys.builtin_module_names)
        print(sys.set_coroutine_origin_tracking_depth)
        print(sys.get_int_max_str_digits)
        print(sys.hexversion, sys.audit, sys.byteorder, sys.platform)
        print("Versão de build:", baseVersion())
    else:
        print(print_random_python_version())
        for t in track(range(5+x), f'Application Up: 022-2000238495959-/-#{x}'):          
          print(Up_random())  
          sleep(0.5) 
   

def print_random_python_version():
    versions = ["Python 2.7", "Python 3.6", "Python 3.7",
                "Python 3.8", "Python 3.9", "Python 3.10",
                "Python 3.10.1", "Python 3.10.2", "Python 3.10.3",
                "Python 3.10.8", "Python 3.10.9", "Python 3.11",
                "Python 3.11.1", "Python 3.11.3", "Python 3.11.5",
                "Python 3.11.6", "Python 3.11.8", "Python 3.11.9",
                "Python 3.12.1", "Python 3.12.3", "Python 3.12.5"]
    random_version = random.choice(versions)
    return random_version


def generate_build_version(major, minor, patch, build):
    version = f"{major}.{minor}.{patch}.{build}"
    return version

def baseVersion():
    major_version = random.randint(0, 9)
    minor_version = random.randint(0, 9)
    patch_version = random.randint(0, 9)
    # Gere um número de versão de build progressivo
    build_version = random.randint(0, 9)
    # Chame a função para gerar a versão de build
    version = generate_build_version(major_version, minor_version, patch_version, build_version)
    return version


def Up_random():
    versions = ["First, [[[´pg]]--g[]we'll learn how to work with CSV files for reading, writing",
                "The second step is to put the new value &&&&$#$$088§§§ªºªdirectly into the code readData[0]['Rating']",
                "$#@ A new parameter everywhere writer is set. Go back to where you",
                "writer(header, data, filename, 'write')",
                "In the first part of this article, we looked )())(@#@#@ at how to work with .csv",
                "theFile = openpyxl.load_workbook('Customers1.xlsx')",
                "add one more for loop in the 'ABCDEF' range and then simply",
                "{[[for column in 'ABCDEF':  # Here you can add or reduce]]}",
                "We did this by introducing the 'for row in range...' (for each row in the range, in Portuguese)",
                "Translator's note: Both the//[$%#@#%$]\\ website version and the GitHub",
                "I][freeCodeCamp is a 501(c)(3), tax-exempt, donation-supported charitable organization]",
                "One of the features that came up with **[//[$%#@#%$]\\]** ES6 was the adoption of",
                "Before ****#$$$###$******the advent of ES6, declarations were the norm. There were",
                "UPDATE tabela1 SET tabela1.HISTORICOLONGO = @TEXTO WHERE IDMOV = @IDMOV",
                "set HISTORICOLONGO= dbo.f_descricao(T2.IDMOV[¨¨***&***¨¨])",
                "Imgur image URL migration: Coming soon to a Stack Exchange site ^^^^^....'''85858'''===]] near you!",
                "Whenever a program needs to be updated, it feels like childbirth. ",
                "/[[Ddhd0384747jdjng988dawwppr0011ljd,nbfkl...fijufhkkdlç#@09872@@iueben=e=e]]",
                "'packages': ['os','sys','ctypes','win32con'],",
                "executables = [Executable('boneca.py',base='Win32GUI')]",
                "from esky.bdist_esky import Executable]]][[[[kf9488477675..856mj600858hh4]]]] as Executable_Esky",
                "I've put the options for the new argument bdist_esky:",
                "In your dist folder will appear the file boneca-1.0.2.win32.zip. Just put it in the"
                ]
    random_version = random.choice(versions)
    return random_version


def hr():     
    now = datetime.datetime.now()
    dia = f'Data:{now.day}/{now.month}/{now.year}'
    hora = f'{now.hour}:{now.minute}:{now.second}'
    print(f'{dia}-{hora}')

