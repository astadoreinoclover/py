from PIL import Image

arq = 'figura.jpg'

im = Image.new("RGB", (400, 400), (255, 255, 0))

# for col in range(400):
#     im.putpixel((col,0), (0, 0, 255))
#     im.putpixel((col,1), (0, 0, 255))
#     im.putpixel((col,2), (0, 0, 255))
#     im.putpixel((col,3), (0, 0, 255))
#     im.putpixel((col,4), (0, 0, 255))
for col in range(400):
    for lin in range(200):
        im.putpixel((col,lin), (0, 0, 255))
im.show()