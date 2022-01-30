import os
infn = False
end = False
while end == False:
    infn = False
    ccmd = input ('custom command: ')
    while infn == False:
        ecode = input('python code to run(use os.system() to run system commands): ')
        if ecode == 'exitc':
            exit()
        if ecode == 'mlc.':
            fline = 1
            while infn == False:
                ecode = input ('code: ')
                indt = input ('Does the code need indentation?(y/n): ')
                if ecode == 'exitc':
                    exit()
                if ecode == 'infn.':
                    fline = 2
                    infn = True
                if fline == 1:
                    os.system ('echo     if cmd == \'' + ccmd + '\': >> command.py')
                    os.system ('echo         ' + ecode + ' >> command.py')
                    fline = 3
                if fline == 0:
                    if indt == 'y':
                        os.system ('echo             ' + ecode + ' >> command.py')
                    else:
                        os.system ('echo         ' + ecode + ' >> command.py')
                if fline == 3:
                    fline = 0
