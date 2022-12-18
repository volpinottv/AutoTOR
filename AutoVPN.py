# Made By Volpino

import time
import os
import subprocess

# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"


try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    print('pip3 non esiste sul dispositivo')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print('pip3 installato correttamente')



try:

    import requests
except Exception:
    print('python3 requests non esiste sul dispositivo')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('python3 requests installato correttamente ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('Tor non esiste nel dispositivo!')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('Tor installato correttamente')

os.system("clear")
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print ('Il tuo ip è cambiato in: '+str(ma_ip()))

print('''\033[0;31m\n
    █████████   █████  █████ ███████████    ███████       █████   █████ ███████████  ██████   █████
   ███░░░░░███ ░░███  ░░███ ░█░░░███░░░█  ███░░░░░███    ░░███   ░░███ ░░███░░░░░███░░██████ ░░███ 
  ░███    ░███  ░███   ░███ ░   ░███  ░  ███     ░░███    ░███    ░███  ░███    ░███ ░███░███ ░███ 
  ░███████████  ░███   ░███     ░███    ░███      ░███    ░███    ░███  ░██████████  ░███░░███░███ 
  ░███░░░░░███  ░███   ░███     ░███    ░███      ░███    ░░███   ███   ░███░░░░░░   ░███ ░░██████ 
  ░███    ░███  ░███   ░███     ░███    ░░███     ███      ░░░█████░    ░███         ░███  ░░█████ 
  █████   █████ ░░████████      █████    ░░░███████░         ░░███      █████        █████  ░░█████
 ░░░░░   ░░░░░   ░░░░░░░░      ░░░░░       ░░░░░░░            ░░░      ░░░░░        ░░░░░    ░░░░░ 

-------------------------------------------"MADE BY VOLPINO"---------------------------------------
''')

time.sleep(1)
print("\033[0;31mBenvenuto su AutoVPN!")

time.sleep(3)
print("\033[0;31mProgramma in avvio. . .")

time.sleep(6)
print("\033[0;31mProgramma avviato con successo!\n")

time.sleep(1)
print("\033[0;31mCambia la tua proxy in: 127.0.0.1:9050 \n")
os.system("service tor start")
x = input("Cambio di ip in secondi {esempio=60} -> ")
lin = input("Quante volte vuoi cambiare il tuo ip {esempio=1000} cambio ip illimitato digita {0} -> ")
if int(lin) ==int(0):

	while True:
		try:
			time.sleep(int(x))
			change()
		except KeyboardInterrupt:

		 	print('\033[0;31m\nAutoVPN CHIUSA CORRETTAMENTE')
		 	quit()

else:
	for i in range(int(lin)):
		    time.sleep(int(x))
		    change()
