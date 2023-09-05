from PIL import Image, ImageDraw

arq = 'figura.jpg'

im = Image.new("RGB", (700, 400), (255, 255, 0))

triangulo = ImageDraw.Draw(im)

for col in range(700):
    for lin in range(133):
        im.putpixel((col,lin), (213, 43, 30))
    for lin in range(134, 266):
        im.putpixel((col,lin), (255, 255, 255))
    for lin in range(267, 400):
        im.putpixel((col,lin), (0, 0, 0))

pontos = [(0, 0), (0, 400), (200, 400 // 2)]
triangulo.polygon(pontos, fill=(1, 138, 44))


im.show()
