from PIL import Image
img = Image.open(r"C:\Python37/2.jpg")
img2 = img.copy()
for km in range(1, 10):
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
            r = round((r * 1 + r1 * 0.5 + r3 * 0.75 + r4 * 0.75 + r7 * 0.75 + r8 * 0.75 + r2 * 0.5 + r5 * 0.5 + r6 * 0.5) / 6)
            g = round((g * 1 + g1 * 0.5 + g3 * 0.75 + g4 * 0.75 + g7 * 0.75 + g8 * 0.75 + g2 * 0.5 + g5 * 0.5 + g6 * 0.5) / 6)
            b = round((b * 1 + b1 * 0.5 + b3 * 0.75 + b4 * 0.75 + b7 * 0.75 + b8 * 0.75 + b2 * 0.5 + b5 * 0.5 + b6 * 0.5) / 6)
            img.putpixel((i, j), (r, g, b))
    img.show()