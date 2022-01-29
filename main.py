import os
infn = False
ccmd = input ('custom command: ')
pt = input ('executable type: ')
while infn == False:
    ecode = input('python code to execute: ')
    if ecode == 'infn.':
        infn = True
    else:
        os.system('echo ' + ecode + ' >> modules\\' + ccmd + '.' + pt)
