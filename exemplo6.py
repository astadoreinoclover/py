from PIL import Image
import numpy as np
a = np.zeros((5, 5))
a[2] = [255, 255, 255, 255, 255]
a[0][2] = 255
a[1][2] = 255
a[3][2] = 255
a[4][2] = 255
print(a)
im = Image.fromarray(a)
im.show()