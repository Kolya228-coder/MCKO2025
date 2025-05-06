from itertools import *
count = 0
for elem in product('АВЕНС', repeat = 4):
    s = ''.join(elem)
    count += 1
    if s.count('Е') == 0 and 'АА' not in s:
        print(count)
        break