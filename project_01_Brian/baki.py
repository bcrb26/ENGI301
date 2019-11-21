"""
--------------------------------------------------------------------------
Servo Control using a Potentiometer
--------------------------------------------------------------------------
License:   
Copyright 2019 - Brian Chen

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
Code to run a computer vision (OpenCV) controlled, target tracking Nerf
cannon. Tracks based on color, finds the centroid of largest object of
that color on screen at any given moment, finds the pixel distance from the
center of camera viewframe, and formulates servo commands accordingly so
that the turret pans and tilts to align with the target location. GPIOs and
MOSFETs are used to run flywheels that fire the Nerf foam balls.

--------------------------------------------------------------------------
"""
import time
from time import sleep
import cv2 # OpenCV
import numpy as np #so I can do math
import socket # to find IP address
from adafruit_servokit import ServoKit # to control servos via PiHat
from grove_rgb_lcd import * #interface with Grove's RGB LCD screen I had

# Find IP Address
def get_ip_address():
 ip_address = '';
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 s.connect(("8.8.8.8",80))
 ip_address = s.getsockname()[0]
 s.close()
 return ip_address

# Initialize Adafruit Servo Hat, xposition, yposition variables
kit = ServoKit(channels = 16)
yposition = 90 # set to default position on program start
xposition = 90 # degrees
kit.servo[4].angle = yposition
kit.servo[12].angle = xposition

# Display IP Address on Grove LCD Display
setText(get_ip_address())
setRGB(0,0,255)

# Open CV Begins here
cap = cv2.VideoCapture(0) #initialize camera
cap.set(3, 480) #set width
cap.set(4, 320) #set height
w = 480 #width defined explicitly for calculation purposes later
h = 320 #height defined explicitly for calculation purposes later
a = 60 #x direction 'tolerance' value - ez adjust
b = 40 #y direction 'tolerance' value - ez adjust

_, frame = cap.read() #capture single frame to set up coordinate system
rows, cols, _ = frame.shape

x_center = int(cols / 2) # x-center of screen
y_center = int(rows / 2) # y-center of screen
x_centroid = int(cols / 2) # start targeting at center of screen
y_centroid = int(rows / 2) # start targeting at center of screen   

setRGB(255,0,0)
setText("Shoot to Thrill") #yeah baby

while True: #always true - always runs, similar to void loop in C
    
    _, frame = cap.read() #continuously capture frames (AKA video)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convert from BGR to HSV color space
    
    #hsv color - 'laser' in variable names a holdover from when I planned on using lasers to target
    low_laser = np.array([31, 0, 0]) #low HSV boundary condition
    high_laser = np.array([179, 255, 255]) #high HSV boundary condition
    laser_mask = cv2.inRange(hsv_frame, low_laser, high_laser) #masks out everything but colors in boundary range
    _, contours, _ = cv2.findContours(laser_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #sorts for largest object of specified color
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)# same thing
    
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        x_centroid = int((x + x + w) / 2)
        y_centroid = int((y + y + h) / 2)
        break #out of the for loop
    #Drawing a 'targeting reticle' for test and debug purposes - will comment out in actual use to save RAM
    cv2.line(frame, (x_centroid, 0), (x_centroid, 320), (0, 255, 0), 2)
    cv2.line(frame, (000, y_centroid), (480, y_centroid), (0, 255, 0), 2)
    cv2.line(frame, (x_center - b, 0), (x_center - b, 320), (0, 0, 255), 3)
    cv2.line(frame, (x_center + b, 0), (x_center + b, 320), (0, 0, 255), 3)
    cv2.line(frame, (0, y_center - a), (480, y_center - a), (0, 0, 255), 3)
    cv2.line(frame, (0, y_center + a), (480, y_center + a), (0, 0, 255), 3)
#     cv2.imshow("Frame", frame) #show camera view with targeting lines superimposed
    cv2.imshow("mask", laser_mask) #show mask view

# X Servo Command
    if (x_centroid < x_center -b) and (xposition >= 5):
        xposition -= 5
#         sleep(.01)
    elif (x_centroid > x_center +b) and (xposition <= 175):
        xposition += 5
#         sleep(.01)
    elif (x_centroid > x_center -b) and (x_centroid < x_center +b):
        xposition += 0
        sleep(.5)
    else:
        xposition += 0

# Y Servo Command
    if (y_centroid < y_center -a) and (yposition >= 50):
            yposition -= 3
            sleep(.25)
    elif (y_centroid > y_center +a) and (yposition <=140 ):
            yposition += 3
            sleep(.25)
    elif (y_centroid > y_center -a) and (x_centroid < x_center +60):
            yposition += 0
            sleep(.5)
    else:
        yposition += 0
        
# Execute Servo Commands
    kit.servo[4].angle = yposition    
    kit.servo[12].angle = xposition
    yposition = yposition
    
    key = cv2.waitKey(1)
    if key == 27:
        break #break out of while loop 
#Shutdown Procedures
cap.release()
cv2.destroyAllWindows()
kit.continuous_servo[12].throttle = 0
setRGB(0, 0, 0)
