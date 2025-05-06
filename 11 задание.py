for x in range(12):
    a = '154' + str(x) + '3'
    b = '1' + str(x) + '365'
    a1 = int(a, 12)
    b1 = int(b, 12)
    if (a1 + b1) % 13 == 0:
        print((a1 + b1) // 13)