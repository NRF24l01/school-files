for i in range(1, 20):
    found = False

    for j in range(2, i):
        if i % j == 0:
            found = True
            break
        if not found:
            print(i, end="  ")