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

''' Perspective Transform:
file = "/Users/salavat/Pictures/cards.jpeg"
img = cv2.imread(file)

cv2.line(img, (526, 85), (627, 220), (0, 255, 0), 2)    # Top
cv2.line(img, (423, 354), (320, 211), (0, 255, 0), 2)   # Bottom
cv2.line(img, (627, 220), (423, 354), (0, 0, 255), 2)   # Left
cv2.line(img, (320, 211), (526, 85), (0, 0, 255), 2)    # Right

width = 250
height = 350

pts1 = np.float32([[526, 85], [627, 220], [320, 211], [423, 354]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Original", img)
cv2.imshow("Perspective Transformation", imgOutput)

cv2.waitKey(0)
'''

''' Display two img in Vertical and Horizontal:
file = "/Users/salavat/Pictures/men.jpeg"
img = cv2.imread(file)

imgHorizontal = np.hstack((img, img))
imgVertical = np.vstack((img, img))

cv2.imshow("Horizontal", imgHorizontal)
cv2.imshow("Vertical", imgVertical)

cv2.waitKey(0)
'''

''' Detect COLOR and use MASK in the image
# Detect COLOR in the image
# To know:
#   1. HSV (Hue, Saturation, Value) https://tr.wikipedia.org/wiki/HSL_ve_HSV

def empty(a):
    pass


mokey = "/Users/salavat/Pictures/monkey.jpg"            # 0	179	0	255	60	249
sport_car = "/Users/salavat/Pictures/car.jpeg"
flower_max = "/Users/salavat/Pictures/flower_max.webp"  # 143	179	18	255	93	249

cv2.namedWindow(winname="TrackBars")
cv2.resizeWindow(winname="TrackBars", width=640, height=240)

cv2.createTrackbar("Hue Min", "TrackBars", 143, 179, empty)     # Hue
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)     # Hue
cv2.createTrackbar("Sat Min", "TrackBars", 18, 255, empty)      # Saturation
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)     # Saturation
cv2.createTrackbar("Val Min", "TrackBars", 93, 255, empty)      # Value
cv2.createTrackbar("Val Max", "TrackBars", 249, 255, empty)     # Value

while True:
    img = cv2.imread(flower_max)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(f'\t{h_min}\t{h_max}\t{s_min}\t{s_max}\t{v_min}\t{v_max} ')

    lower_value = np.array([h_min, s_min, v_min])
    upper_value = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lowerb=lower_value, upperb=upper_value, dst=None)

    imgResult = cv2.bitwise_and(src1=img, src2=img, mask=mask)

    cv2.imshow("IMAGE Original Color", img)
    cv2.imshow("IMAGE HSV Color", imgHSV)
    cv2.imshow("IMAGE Mask", mask)
    cv2.imshow("IMAGE Mask Result", imgResult)

    cv2.waitKey(1)
'''

# '''CONTOURS / SHAPE DETECTION
# CONTOURS / SHAPE DETECTION, chapter 8:
# URL: https://youtu.be/WQeoO7MI0Bs?t=4540
def get_contours(image):
    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(f"\nArea is:\t\t{area}")

        if area > 500:
            cv2.drawContours(imgContur, contours=cnt, contourIdx=-1, color=(255, 0, 0), thickness=2)
            perimeter = cv2.arcLength(cnt, closed=True)
            print(f"Perimeters is:\t\t{round(perimeter, 2)}")

            approximately = cv2.approxPolyDP(cnt, epsilon=0.02*perimeter, closed=True)
            object_corner = len(approximately)
            print(f"Approximately is: \t{object_corner}")

            x, y, w, h = cv2.boundingRect(approximately)

            if object_corner == 3:
                object_type = "Triangle"
            elif object_corner == 4:
                aspect_ratio = w / h
                if 0.95 < aspect_ratio < 1.05:
                    object_type = "Sqare"
                else:
                    object_type = "Rectangle"
            elif object_corner > 4:
                object_type = "Circle"
            else:
                object_type = "Unknown"

            cv2.rectangle(imgContur, pt1=(x, y), pt2=(x+w, y+h), color=(0, 255, 0), thickness=2)
            cv2.putText(img=imgContur, text=object_type,
                        org=(x + 10, y + h - 10),
                        fontFace=cv2.FONT_HERSHEY_COMPLEX,
                        fontScale=0.5, color=(0, 0, 0),
                        thickness=1)

shapes = "/Users/salavat/Pictures/shapes.jpeg"
img = cv2.imread(shapes)
imgContur = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, ksize=(7, 7), sigmaX=1)
imgCanny = cv2.Canny(image=imgBlur, threshold1=50, threshold2=50)
imgBlank = np.zeros_like(img)

get_contours(imgCanny)

cv2.imshow("Picture ORIGINAL", img)
cv2.imshow("Picture GRAY", imgGray)
cv2.imshow("Picture BLUR", imgBlur)
cv2.imshow("Picture CANNY", imgCanny)
cv2.imshow("Picture BLANK", imgBlank)
cv2.imshow("Picture CONTUR", imgContur)

cv2.waitKey(0)
# '''

# FACE DETECTION
# URL: https://youtu.be/WQeoO7MI0Bs?t=6033