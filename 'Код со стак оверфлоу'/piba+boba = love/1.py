text = input("Введите строку:")
i = 0
l = len(text)
while i <= l:
    print(text)
    text = text[:len(text) - 1]
    i = i + 1
    #print(i)
    #print(len(text))