import cv2
import numpy as np

'''Show picture:
# Open Picture file
path_to_pic = "/Users/salavat/Pictures/monkey.jpg"
img = cv2.imread(path_to_pic)
cv2.imshow("Output", img)
# 0 - always, 1000 = 1 second
cv2.waitKey(0)
'''

''' Show Video
# Open Video file
path_to_video = "/Users/salavat/Movies/Road-Construction.mp4"
capture = cv2.VideoCapture(path_to_video)
while True:
    success, img = capture.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

''' Connect to WebCam video
# Connect to WebCam
capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)
capture.set(10, 100)

while True:
    success, img = capture.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

''' Convert Picture, work with COLOR
# Convert picture to GRAY, BLUR, CANNY, DIALATION
path_to_pic = "/Users/salavat/Pictures/men2.jpeg"
img = cv2.imread(path_to_pic)
kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
'''

''' Crop Image:
# https://youtu.be/WQeoO7MI0Bs?t=2060
file = "/Users/salavat/Pictures/car.jpeg"

img = cv2.imread(file)
img_Resized = cv2.resize(img, (600*2, 430*2))

print(img.shape)
print(img_Resized.shape)

img_Cropped = img[117:309, 8:593]

cv2.imshow("Image Original", img)
# cv2.imshow("Image Resized", img_Resized)
cv2.imshow("Image Cropped", img_Cropped)

cv2.waitKey(0)
'''

''' Put the Line, Rectangle, Circle, Text:
# file = "/Users/salavat/Pictures/car.jpeg"
img = np.zeros((512, 512, 3), np.uint8)

# Line: (x,y), finish(x,y), RGB Color(Blue,Green,Red, Line Thickness
cv2.line(img, (10, 500), (510, 375), (0, 255, 0), 2)
# Rectangle: (x,y), finish(x,y), RGB Color(Blue,Green,Red, Line Thickness
cv2.rectangle(img, (450, 80), (500, 30), (119, 119, 119), 1)
# Solid Rectangle: (x,y), finish(x,y), RGB Color(Blue,Green,Red), FILLED
cv2.rectangle(img, (450, 180), (500, 130), (119, 255, 119), cv2.FILLED)
# Filled Circle: Center(x,y), Radius(x,y), RGB Color(Blue,Green,Red), FILLED
cv2.circle(img, (250, 250), 50, (0, 255, 255), cv2.FILLED)
# Put Text
cv2.putText(img, "The Circle", (150, 180), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 150, 0), thickness=1)

cv2.imshow("Line, Rectangle, Circle and Text", img)
cv2.waitKey(0)
'''

