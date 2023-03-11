from PIL import Image
img = Image.open("Без названия.jpeg")
img2 = img.copy()
for i in range(1, img.width-1):
    for j in range(1, img.height-1):
        r, g, b = img2.getpixel((i, j))
        r1, g1, b1 = img2.getpixel((i-1, j-1))
        r2, g2, b2 = img2.getpixel((i-1, j+1))
        r3, g3, b3 = img2.getpixel((i-1, j))
        r4, g4, b4 = img2.getpixel((i+1, j))
        r5, g5, b5 = img2.getpixel((i+1, j+1))
        r6, g6, b6 = img2.getpixel((i+1, j-1))
        r7, g7, b7 = img2.getpixel((i, j-1))
        r8, g8, b8 = img2.getpixel((i, j+1))
        r = round((r * 9 + r1 * (-1) + r3 * (-1) + r4 * (-1) + r7 * (-1) + r8 * (-1) + r2 * (-1) + r5 * (-1) + r6 * (-1)) / 1)
        g = round((g * 9 + g1 * (-1) + g3 * (-1) + g4 * (-1) + g7 * (-1) + g8 * (-1) + g2 * (-1) + g5 * (-1) + g6 * (-1)) / 1)
        b = round((b * 9 + b1 * (-1) + b3 * (-1) + b4 * (-1) + b7 * (-1) + b8 * (-1) + b2 * (-1) + b5 * (-1) + b6 * (-1)) / 1)
        img.putpixel((i, j), (r, g, b))
img.show()