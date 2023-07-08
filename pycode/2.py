import cv2 
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np 
from PIL import Image
import numpy as np
#importimport os
import argparse
import cv2
import numpy as np
import sys
import glob
import importlib.util 
import tensorflow as tf




img1 = cv2.imread('/home/pi/raspbianlegacy/pic/353.jpg')
#img1 = cv2.resize(img1, (780, 480))
img1 = img1[ 505:611, 103:319]
img11 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
img1 = cv2.GaussianBlur(img11,(13,13), 0)

#img1 = cv2.Canny(img1, 100, 200)
img1 = cv2.dilate(img1, None, iterations=5)
img1 = cv2.erode(img1, None, iterations=3)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


(thresh, blackAndWhiteImage) = cv2.threshold(img1, 200, 255, cv2.THRESH_BINARY)
img_neg = cv2.bitwise_not(blackAndWhiteImage)

digi1 = img_neg[0:106,0:68]
digi2 = img_neg[0:106,77:121]
digi3 = img_neg[0:106,138:216]

img6 = cv2.resize(digi3, (28, 28))
#img6 = (255 - img6) - 128
cv2.imshow('Frame33', img6)

def ocrtest(img):

    

    img = cv2.resize(img, (28, 28))
    img = (255 - img) - 128

    # img = img.astype(np.uint8)
    img = img.astype(np.int8)
    
    input_tensor = img.reshape(1, img.shape[0], img.shape[1], 1)
    input_tensor = tf.convert_to_tensor(input_tensor)

    interpreter = tf.lite.Interpreter(model_path="conv_mnist_quant.tflite")
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # set input tensor
    interpreter.set_tensor(input_details[0]['index'], input_tensor)

    # Inference
    interpreter.invoke()

    scores = interpreter.get_tensor(output_details[0]['index'])
    result = np.argmax(scores[0])

    print("predicted number is {} [{:.2f}]".format(result, scores[0][result]))

ocrtest(digi1)














#cv2.imshow('Frame1', blackAndWhiteImage)
cv2.imshow('Frame2', img_neg)
cv2.imshow('digit-1', digi1)
cv2.imshow('digit-2', digi2)
cv2.imshow('digit-3', digi3)
#cv2.imwrite('/home/pi/raspbianlegacy/pic/0000.jpg', img_neg)



temp = pytesseract.image_to_string(img_neg)
print(temp)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows()
