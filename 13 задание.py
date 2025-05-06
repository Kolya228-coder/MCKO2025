file = open('13.txt').readlines()
int_file = []
cr = []
itog = []
for line in file:
    int_file.append(int(line))
for elem in int_file:
    if elem % 15 != 0:
        cr.append(elem)
n = min(cr)
for i in range(len(int_file) - 1):
    if int_file[i] % n == 0 and int_file[i + 1] % n == 0:
        itog.append(int_file[i] + int_file[i + 1])
print(len(itog), max(itog))