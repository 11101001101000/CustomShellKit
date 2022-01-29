import os
end = False
print ('CustomShellKit default shell 0.1')
print ('This shell runs executable files in modules folder')
while end == False:
    cmd = input ('command: ')
    pt = input ('executable type: ')
    if pt == 'py':
        os.system ('python modules\\' + cmd + '.py')
    if pt == 'bat':
        os.system ('modules\\' + cmd + '.bat')
    if pt == 'cmd':
        os.system (cmd)
    if pt == 'ps':
        os.system ('powershell -Command ' + cmd)
