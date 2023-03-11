import random

def color_noise(img):
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))

            r += random.randint(-150, 150)
            g += random.randint(-150, 150)
            b += random.randint(-150, 150)

            img.putpixel((i, j), (r, g, b))

def grayscale(img):
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))

            average = (r + g + b) // 3

            img.putpixel((i, j), (average, average, average))

# тут будут другие фильтры