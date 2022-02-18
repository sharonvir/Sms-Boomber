from time import sleep
from colorama import Fore as color
import sys, os



def banner():
    print(color.LIGHTRED_EX+"""
        
  __  __ _____    _____ ____  ______ _  _  __ ______ 
 |  \/  |  __ \  |  __ \___ \|  ____| || |/_ |____  |
 | \  / | |__) | | |  | |__) | |__  | || |_| |   / / 
 | |\/| |  _  /  | |  | |__ <|  __| |__   _| |  / /  
 | |  | | | \ \ _| |__| |__) | |       | | | | / /   
 |_|  |_|_|  \_(_)_____/____/|_|       |_| |_|/_/    
                                                     
                                                
                                                               version 1.0""")

    sleep(0.1)

    print(color.RED+"""
------------------------------------------------------
|||           Developer: MR.D3F417                 |||
|||           Contact: mrrobotha3@gmail.com        |||  
|||           Discord : discord.gg/KsskgvE48z      |||             
------------------------------------------------------             
""")
    sleep(0.1)


def menu_respaws():
    try:
        print(color.RED+"[1] "+ color.LIGHTYELLOW_EX+"Sms-Bomber")
        print(color.CYAN+"*********************")
        sleep(0.1)
        
        print(color.RED+"[0] "+ color.LIGHTYELLOW_EX+"Exit")
        print(color.CYAN+"*********************")
        sleep(0.1)
    except:
        print(color.RED+"[-] Something Went Wrong....")
        sleep(1)
        sys.exit()
