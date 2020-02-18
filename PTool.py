from colorama import Fore, Back, Style
import time
from tqdm import tqdm
import os
import sys


print(Fore.RED + ''' /$$$$$$$  /$$$$$$                       /$$               /$$ /$$
| $$__  $$|_  $$_/                      | $$              | $$| $$
| $$  \ $$  | $$   /$$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ | $$| $$
| $$$$$$$/  | $$  | $$__  $$ /$$_____/|_  $$_/   |____  $$| $$| $$
| $$____/   | $$  | $$  \ $$|  $$$$$$   | $$      /$$$$$$$| $$| $$
| $$        | $$  | $$  | $$ \____  $$  | $$ /$$ /$$__  $$| $$| $$
| $$       /$$$$$$| $$  | $$ /$$$$$$$/  |  $$$$/|  $$$$$$$| $$| $$
|__/      |______/|__/  |__/|_______/    \___/   \_______/|__/|__/
                                                                  
                                                                  
                                                                  ''')                                                                                                          
print(Style.RESET_ALL)

def showMenu():
	from modules.menu import menu
time.sleep(3)
showMenu()

showMenu()
print(Style.RESET_ALL)
choise = input(Fore.RED + 'root@kali' + Fore.WHITE + ':' + Fore.BLUE + '~' + Fore.WHITE + '# ')
print(Style.RESET_ALL)

if choise == '1':
	os.system("apt install python && apt install python3 && apt install git && apt install python3-pip && apt install nmap")

