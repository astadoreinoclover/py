from PIL import Image
im = Image.open("laranjal.jpg")

box = (788, 728, 1292, 1381)
region = im.crop(box)

region.show()