import cv2

# imread()载入图像
# imwrite()输出图像到文件
# imshow()显示图像
image = cv2.imread('MyPic.png')
cv2.imwrite('MyPic.jpg', image)  # 将.png图像转换为.jpg