import cv2
vid = cv2.VideoCapture('bad_apple.mp4')
success,image = vid.read()
c = 0
while success:
  cv2.imwrite("frame%d.jpg" % c, image)    # save frame as JPEG file
  success,image = vid.read()
  c += 1