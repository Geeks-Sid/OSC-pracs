import numpy as np
import cv2

im = open(r'C:\Users\Geeks_Sid\Pictures\pic.jpg')
temp = im
im = 255 - im
cv2.imwrite(r'C:\Users\Geeks_Sid\Pictures\negative.jpg', im)

t = np.zeros((960, 960), int)

for i in range(960):
    for j in range(960):
        t1 = temp[i][j][0]
        t2 = temp[i][j][1]
        t3 = temp[i][j][2]
        t[i][j] = 0.21*t1 + 0.72*t2 + 0.07*t3
cv2.imwrite(r'C:\Users\Geeks_Sid\Pictures\bnw.jpg', t)
