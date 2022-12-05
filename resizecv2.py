#python image resize
import cv2
import sys
img = cv2.imread('E:\Ripm2\web\worldtree.png', cv2.IMREAD_UNCHANGED)
scale_percent= 0.5
#width = int(img.shape[1] * scale_percent )
#height = int(img.shape[0] * scale_percent)
width=int(img.shape[1]*0.05)
height = int(img.shape[0]*0.089)
din = (width,height)

resized = cv2.resize(img,din,interpolation=cv2.INTER_AREA)

print("Resize Image",resized)

cv2.imshow('Resized image',resized)
cv2.imwrite('E:\Ripm2\web\ssess.png',resized) #'\r' is actaully a keyword lol write something else interesting
cv2.waitKey(0)
cv2.destroyAllWindows()

