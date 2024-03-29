# CHALLENGE
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2		
import numpy as np
import random

# Ouvrir l'image

img_rgb = Image.open('coins.bmp')
img_gray = img_rgb.convert('L') 
img_gray.save('W.png')
image1 = cv2.imread('W.png') 
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) 
ret, thresh1 = cv2.threshold(img, 120, 255, 
                             cv2.THRESH_OTSU) 

# Conversion en greyscale
#Application du treshold pour permettreune meilleur lecture
# __
def segmentation(img):
    sx, sy= img.shape
    region = np.zeros((sx, sy))
    nb_region = 1
    test_new_region = 0
    i = 0
    for x in range(sx - 1):
        for y in range(sy - 2):
            if img[x+1, y+1] == 255:
                if img[x, y+2] != 0:
                    region[x+1, y+1] = region[x, y+2]
                elif img[x, y+1] != 0:
                    region[x+1, y+1] = region[x, y+1]
                    test_new_region = test_new_region + 1
                elif img[x, y] != 0:
                    region[x+1, y+1] = region[x, y]
                    test_new_region = test_new_region + 1
                elif img[x+1, y] != 0:
                    region[x+1, y+1] = region[x+1, y]
                    test_new_region = test_new_region + 1
                else:
                    region[x + 1, y + 1] = nb_region
                    nb_region = nb_region+0.1
                    test_new_region = 1
            else:
                test_new_region = 0
    return region
# __

#Application de le segmentation
region = segmentation(thresh1)

# Affichage
plt.imshow(img_rgb)
plt.show()
plt.imshow(img_gray)
plt.show()	
plt.imshow(thresh1)
plt.show()	
plt.imshow(region)
plt.show()