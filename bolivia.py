from PIL import Image

arq = 'figura.jpg'

im = Image.new("RGB", (700, 400), (255, 255, 0))

for col in range(700):
    for lin in range(133):
        im.putpixel((col,lin), (213, 43, 30))
    for lin in range(134, 266):
        im.putpixel((col,lin), (249, 227, 0))
    for lin in range(267, 400):
        im.putpixel((col,lin), (0, 121, 52))


im.show()