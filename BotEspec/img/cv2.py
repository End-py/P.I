import cv2
import os
import sys

#os.system('cls')

#print(cv2.subtract(cv2.imread(sys.argv[1]), cv2.imread(sys.argv[2])).any())

im1 = cv2.imread(sys.argv[1])

for dirpath, _, filenames in os.walk(sys.argv[2]):
    for filename in filenames:
        path = os.path.join(dirpath, filename)
        if filename.endswith('.jpg'):
            try:
                im2 = cv2.imread(path)
                diff1 = cv2.subtract(im1, im2)
                diff2 = cv2.subtract(im2, im1)
                if not diff1.any() and not diff2.any():
                    print(path)
            except cv2.error:
                pass
