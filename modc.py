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
        os.system ('echo ' + ecode + ' >> ' + mn + '.' + ext)
