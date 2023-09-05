from PIL import Image
im = Image.open("laranjal.jpg")

# out = im.rotate(45)
out = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
out.show()