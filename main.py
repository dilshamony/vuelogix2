import cv2
import numpy as np

#Image type are Colour
Image1=cv2.imread('assets/Reference image.png', 1)
Image2=cv2.imread('assets/Test image.png', 1)


# Image type are greyscale
# ========================
# Image1=cv2.imread('assets/Reference image.png', 0)
# Image2=cv2.imread('assets/Test image.png', 0)


# Image type are unchanged
# ========================
# Image1=cv2.imread('assets/Reference image.png', -1)
# Image2=cv2.imread('assets/Test image.png', -1)


# Image comparison
if Image1.shape==Image2.shape:
    difference = cv2.subtract(Image1, Image2)
    b,g,r=cv2.split(difference)
    if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
        print("0%")
    else:
        print("Images are different")
# Image1=cv2.resize(Image1,(500,500))
# Image2=cv2.resize(Image2,(500,500))
# difference=cv2.resize(difference,(500,500))
cv2.imshow('Reference',Image1)
cv2.imshow('Test',Image2)
cv2.imshow("Difference",difference)
cv2.waitKey(0)
cv2.destroyAllWindows()






# difference=cv2.subtract(Image1,Image2)
# result= not np.any(difference)
# if result is True:
#     print("0%")
# else:
#     cv2.imwrite('result.png',difference)
#     print("Images are different")
