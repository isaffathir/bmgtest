for a in range(1, 116):
    if a % 3 == 0 and a % 5 == 0:
        print("frontend backend",end=',')
        continue
    elif a % 3 == 0:
        print("frontend", end=',')
        continue
    elif a % 5 == 0:
        print("backend", end=',')
        continue
    print(a,end=',')