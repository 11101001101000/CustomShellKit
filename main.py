import os
infn = False
end = False
while end == False:
    infn = False
    ccmd = input ('custom command: ')
    pt = input ('executable type: ')
    while infn == False:
        ecode = input('code to run: ')
        if ecode == 'exitc':
            exit()
        if ecode == 'infn.':
            infn = True
        else:
            os.system('echo ' + ecode + ' >> modules/' + ccmd + '.' + pt)
