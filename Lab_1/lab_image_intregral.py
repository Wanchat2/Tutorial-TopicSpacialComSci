# หา Integral images

import numpy as np
import random

id = 10 # รหัส 3 ตัวท้ายบวกกัน เช่น 064 >> 0 + 6 + 4

im = np.zeros((10, 10, 1), dtype=np.uint8)

random.seed(id)

for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        im[i,j] = random.randint(0, 256)

print(im) # รูปภาพเพื่อทำ images integral 

