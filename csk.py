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
        if ecode == 'infn.':
            infn = True
        else:
            if ecode == '':
                os.system ('echo \'\' >> command.py')
            else:
                os.system ('echo     if cmd == \'' + ccmd + '\': >> command.py')
                os.system ('echo         ' + ecode + ' >> command.py')
