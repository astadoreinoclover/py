from PIL import Image

with Image.open("laranjal.jpg") as im:
    im = im.convert("1")
    im.show()
