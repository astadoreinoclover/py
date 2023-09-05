from PIL import Image
im = Image.open("laranjal.jpg")

print(im.format, im.size, im.mode)
im.show()