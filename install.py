import os
import time
choice = input('\033[1;36m\nPer installare [aut] premi (Y) Per rimuoverlo premi (N) -> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 AutoTOR.py')
    run('mkdir /usr/share/aut')
    run('cp AutoTOR.py /usr/share/aut/AutoTOR.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/AutoTOR.py "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/AutoTOR.py')
    print("\033[1;37m\nAutoTOR INSTALLATA CORRETTAMENTE!")
    time.sleep(1)
    print("\033[1;36m\nPer aprire il programma digita: aut")
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print("\033[1;37m\nComando [aut] rimosso")
    