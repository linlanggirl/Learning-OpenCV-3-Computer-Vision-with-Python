import cv2

grayImage = cv2.imread('MyPic.png', cv2.IMREAD_GRAYSCALE) # 转换为灰度图像
cv2.imwrite('MyPicGray.png', grayImage)
