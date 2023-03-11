cout = int(input("Количество шницелей: "))
best_shnicel = ""
best_mramornah_podjarok = 0

i = 1
while i <= cout:
    name = input("Введите имя шницеля  "+ str(i)  + ": ")
    mram = int(input("Ввыдите количесто мраморных поджарок: "))
    if mram >= best_mramornah_podjarok:
        best_mramornah_podjarok = mram
        best_shnicel = name
    i = i + 1

print("Лучший шницель: "+ best_shnicel)