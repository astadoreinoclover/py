from PIL import Image

arq = 'figura.jpg'

im = Image.new("RGB", (700, 400), (255, 255, 0))

for col in range(700):
    for lin in range(400):
        im.putpixel((col,lin), (213, 43, 30))
    for lin in range(150, 250):
        im.putpixel((col,lin), (256, 256, 256))
    for lin in range(175, 225):
        im.putpixel((col,lin), (0, 0, 256))

for col in range(150, 175):
    for lin in range(0, 400):
        im.putpixel((col,lin), (256, 256, 256))

for col in range(175, 225):
    for lin in range(0, 400):
        im.putpixel((col,lin), (0, 0, 256))

for col in range(225, 250):
    for lin in range(0, 400):
        im.putpixel((col,lin), (256, 256, 256))

for col in range(700):
    for lin in range(175, 225):
        im.putpixel((col,lin), (0, 0, 256))


im.show()