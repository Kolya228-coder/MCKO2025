cr = []
for n in range(1, 1000):
    dvoich = bin(n)[2:]
    if n % 2 == 0:
        result = dvoich + '10'
    else:
        result = '1' + dvoich + '00'
    itog = int(result, 2)
    if itog > 107:
        cr.append(n)
print(min(cr))