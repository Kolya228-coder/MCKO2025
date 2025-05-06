p = 5
q = 7
e = 11
max_d = 40
n = (p - 1) * (q - 1)
for d in range(max_d):
    if (d * e) % n == 1:
        print(d)