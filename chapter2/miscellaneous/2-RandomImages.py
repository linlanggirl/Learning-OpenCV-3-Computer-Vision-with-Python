import cv2
import numpy
import os
# 图像与原始字节码之间的转换；一个字节(占8位)可以表示0到255的整数
# Make an array of 120,000 random bytes.
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByteArray)

# Convert the array to make a 400x300 grayscale image.
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('RandomGray.png', grayImage)

# Convert the array to make a 400x300 color image.
bgrImage = flatNumpyArray.reshape(300, 400, 1)
cv2.imwrite('RandomColor1.png', bgrImage)

# Convert the array to make a 400x300 color image.
bgrImage = flatNumpyArray.reshape(200, 200, 3)
cv2.imwrite('RandomColor2.png', bgrImage)

# Convert the array to make a 400x100 color image.
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('RandomColor.png', bgrImage)