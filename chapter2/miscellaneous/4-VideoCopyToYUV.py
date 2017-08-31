import cv2
# 视频文件的读和写发
# 读取AVI文件的帧，并采用YUV颜色编码将其写入另一个帧中
videoCapture = cv2.VideoCapture('MyInputVid.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'MyOutputVid.avi', cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)
    # cv2.VideoWriter_fourcc('I','4','2','0')表示未压缩的YUV颜色编码，文件扩展名为.avi

success, frame = videoCapture.read()
print frame
while success: # Loop until there are no more frames.
    videoWriter.write(frame)
    success, frame = videoCapture.read()