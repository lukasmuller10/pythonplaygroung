import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Boston', img)

b,g,r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged',merged)

cv.waitKey(0)
