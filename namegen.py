import random

with open("new.txt", "r") as file:
    suffix = file.readline().replace('"','').split(',')
    prefix = file.readline().replace('"','').split(',')
    ele = suffix.pop()

def Maingen(pre, suf, m):
    count = 0
    while count < m:
        first = random.choice(pre)
        last = random.choice(suf)
        print(first, last)
        valid = isValid(first,last)
        print(valid)
        count = count + 1

def isValid(first, last):
    if (first == last) or (first =='silver' and last =='pelt') or (first =='green' and last =='leaf') or \
            (first =='leaf' and last =='fall') or (first =='moon' and (last =='pool' or last =='stone')) or \
            (first =='tall' and (last =='pine' or last == 'rock' )) or (first =='snake' and last =='tongue') or \
            (first =='snake' and last =='tongue'):
        return False
    else:
        return True

max = int(input('Please input how many names you want:'))
Maingen(prefix, suffix, max)
