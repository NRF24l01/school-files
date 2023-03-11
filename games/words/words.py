used = []
w1 = ""
w2 = ""
file = open('words.txt', 'r', encoding='utf8')
all_worlds = file.read().split("""
""")
file.close()

w1 = input("Слово первого игрока: ")
if w1 not in used and w1 in all_worlds:
    used.append(w1)
    print("Отлично!")
    w2 = input("Слово второго игрока: ")
    if w1[-1] == w2[0] and w2 not in used and w2 in all_worlds:
        used.append(w2)
        print("Отлично!")
    else:
        print("Попробуйте ещё раз")

while True:
    w1 = input("Слово первого игрока: ")
    if w1[0] == w2[-1] and w1 not in used and w1 in all_worlds:
        used.append(w1)
        print("Отлично!")
        w2 = input("Слово второго игрока: ")
        if w1[-1] == w2[0] and w2 not in used and w2 in all_worlds:
            used.append(w2)
            print("Отлично!")
        else:
            print("Попробуйте ещё раз")


print(all_worlds)