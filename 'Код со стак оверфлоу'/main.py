from PIL import Image
import random
path = input("Введите путь к файлу: ")
img = Image.open(path).convert("RGB")

def cvshum(img):
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))
            r = r + random.randint(-50, 50)
            g = g + random.randint(-50, 50)
            b = b + random.randint(-50, 50)
            img.putpixel((i, j), (r, g, b))
    img.show()
    save_path = input("Куда сохранить: ")

    img.save(save_path)
    return img

def shum(img):
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))
            r = r + 100
            g = g + 100
            b = b + 100
            img.putpixel((i, j), (r, g, b))
    img.show()
    save_path = input("Куда сохранить: ")

    # сохраняем
    img.save(save_path)
    return img

def in4(img):
    for i in range(img.width // 2, img.width):
        for j in range(img.height // 2):
            r, g, b = img.getpixel((i, j))
            r = r + 256
            img.putpixel((i, j), (r, g, b))
    for i in range(img.width // 2, img.width):
        for j in range(img.height // 2, img.height):
            r, g, b = img.getpixel((i, j))
            g = g + 256
            img.putpixel((i, j), (r, g, b))
    for i in range(img.width // 2):
        for j in range(img.height // 2, img.height):
            r, g, b = img.getpixel((i, j))
            b = b + 256
            img.putpixel((i, j), (r, g, b))
    img.show()
    save_path = input("Куда сохранить: ")

    # сохраняем
    img.save(save_path)
    return img

def KEK(img):
    for i in range(img.width // 2):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))
            img.putpixel((img.width - i - 1, j), (r, g, b))
    img.show()
    return img

def black_white(img):
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))
            if r > 128 and g > 128 and b > 128:
                r = 256
                g = r
                b = r
            else:
                r = 0
                g = r
                b = r
            img.putpixel((i, j), (r, g, b))
    img.show()
    return img

def plen(img):
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))
            r = (r + g + b) // 3
            g = r
            b = r
            img.putpixel((i, j), (r, g, b))
    img.show()
    save_path = input("Куда сохранить: ")

    # сохраняем
    img.save(save_path)
    return img

b = input('ВВЕДИТЕ 1, если хотите воспользоваться редактором цветного шума \nВВЕДИТЕ 2, если хотите воспользоваться редактором шума \nВВЕДИТЕ 3, если хотите тонировать 4 части своей картинке разным цветом \nВВЕДИТЕ 4, если хотите преобразвать фотографию в градации серого цвета \nВВЕДИТЕ 5, если хотите преобразвать фотографию в фотографию, состоящую только из черного и белого')
if b == '1':
    cvshum(img)
elif b == '2':
    shum(img)
elif b == '3':
    in4(img)
elif b =='5':
    black_white(img)
elif b =='4':
    plen(img)
else:
    KEK(img)