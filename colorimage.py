import cv2
import sys

src = cv2.imread('baboon.jpg',cv2.IMREAD_COLOR)
cv2.namedWindow("Original image")
cv2.imshow("Original image", src)

b,g,r = cv2.split(src)
cv2.namedWindow("Red")
cv2.imshow("Red",r)
cv2.namedWindow("Green")
cv2.imshow("Green",g)
cv2.namedWindow("Blue")
cv2.imshow("Blue",b)

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
H,S,V = cv2.split(hsv)
cv2.namedWindow("H")
cv2.imshow("H",H)
cv2.namedWindow("S")
cv2.imshow("S",S)
cv2.namedWindow("V")
cv2.imshow("V",V)

ycc = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
Y,Cr,Cb = cv2.split(ycc)
cv2.namedWindow("Y")
cv2.imshow("Y",Y)
cv2.namedWindow("Cr")
cv2.imshow("Cr",Cr)
cv2.namedWindow("Cb")
cv2.imshow("Cb",Cb)

print("BGR value: ", src[20,25])
print("HSV value: ", hsv[20,25])
print("YCrCb value: ", ycc[20,25])
cv2.waitKey(0)
cv2.destroyAllWindows()
