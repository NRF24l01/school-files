import random
import copy

words = ["ноут","денчик", "мышь", "картошка", "стул", "учитель", "логорифм"]

word = random.choice(words)
wordu = "_"*len(word)
wordu = list(wordu)
#print(word)
#print(wordu)
lifes = 10

def re(list):
    ina = ''
    for i in list:
        ina = ina+i
    return ina

while True:
    word = random.choice(words)
    wordu = "_" * len(word)
    wordu = list(wordu)
    lifes = 10

    while lifes != 0:
        k = input()
        l = copy.deepcopy(wordu)
        for j in range(len(word)):
            if word[j] == k:
                wordu[j] = k
        print(''.join(wordu))
        if wordu == l:
            lifes = lifes - 1

        print("У тебя осталось:", lifes, "попыток")
        if "".join(wordu) == "".join(word):
            print("Победа!")
            break
    print("Играем заново")