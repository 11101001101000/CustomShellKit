print ('type first number in the first row, \'+ - * /\' in the next, and the second number in the last row')
na = input()
nb = input()
nc = input()
if nb == '+':
    print (int(na) + int(nc))
if nb == '-':
    print (int(na) - int(nc))
if nb == '*':
    print (int(na) * int(nc))
if nb == '/':
    print (int(na) / int(nc))
