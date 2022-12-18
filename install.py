import os
choice = input('\033[0;31mPer installarlo premi (Y) Altrimenti premi (N) -> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 AutoVPN.py')
    run('mkdir /usr/share/aut')
    run('cp AutoVPN.py /usr/share/aut/AutoVPN.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/aut/AutoVPN.py "$@"')
    with open('/usr/bin/aut','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/AutoVPN.py')
    print('''\n\nAutoVPN INSTALLATA CORRETTAMENTE! \nfrom now just type \x1b[6;30;42maut\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/aut ')
    run('rm /usr/bin/aut ')
    print('\033[0;31mProcesso annullato')
