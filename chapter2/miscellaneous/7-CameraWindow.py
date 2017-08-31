import cv2

clicked = False
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True
# namedWindow()指定窗口名创建
# imshow()显示
# destoryWindow()销毁窗口
cameraCapture = cv2.VideoCapture(0)  # 获取摄像头
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)

print 'Showing camera feed. Click window or press any key to stop.'
success, frame = cameraCapture.read()
while cv2.waitKey(1) == -1 and not clicked:
    if frame is not None:
        cv2.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('MyWindow')