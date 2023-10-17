import cv2
  
# path
path = r'ref\g1pure2.png'
  
# Using cv2.imread() method
# Using 0 to read image in grayscale mode
img = cv2.imread(path)
print(type(img[1][1]))
# Displaying the image

# cv2.imshow('image', img)
# cv2.waitKey(0)