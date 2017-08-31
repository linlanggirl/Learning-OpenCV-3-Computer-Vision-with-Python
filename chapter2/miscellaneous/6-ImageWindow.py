import cv2
import numpy as np

# 在窗口显示图像
# namedWindow()指定窗口名创建
# imshow()显示
# destoryWindow()销毁窗口
image = cv2.imread('MyPic.png')
image[0, 0] = 255
cv2.imshow("w1", image)
image[:, :, 0] = 255
cv2.imshow("w2", image)  # 第一个参数显示图像的帧名称，第二个参数要显示的图像本身
cv2.waitKey()
cv2.destroyAllWindows()  # 释放由opencv创建的所有窗口
