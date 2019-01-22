import sys
for strInput in sys.stdin:
    try:
        D, I = strInput.split()
        D = int(D)
        I = int(I)

        k = 1
        for i in range(D - 1):
            if I % 2 == 1:
                k = 2 * k
                I = (I + 1) /2
            else:
                k = k * 2 + 1
                I = I / 2
        print(k)
    except:
        exit(0)
