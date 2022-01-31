import os
mn = input ('module name: ')
ext = input ('executable type: ')
sys = input ('windows or unix-like(w/u): ')
infn = 0
while infn == 0:
    ecode = input ('code: ')
    if ecode == 'infn.':
        infn = 1
    else:
        if sys == 'w':
            os.system ('echo ' + ecode + ' >> modules\\' + mn + '.' + ext)
        if sys == 'u':
            os.system ('echo ' + ecode + ' >> modules/' + mn + '.' + ext)
