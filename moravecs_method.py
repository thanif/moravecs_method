import sys
from PIL import Image
import cv2
import os


threshold = 100
         
for name in os.listdir("./images/"):
   
    image = Image.open("./images/"+name).convert("L")

    input_img = cv2.imread("./images/"+name, 0)
    
    cv2.imshow('Input Image', input_img)
    cv2.waitKey(0)

    output_img = cv2.cvtColor(input_img.copy(), cv2.COLOR_GRAY2RGB)

    corners = []
    xy_shifts = [(1, 0), (1, 1), (0, 1), (-1, 1)]

    for y in range(1, image.size[1]-1):
        for x in range(1, image.size[0]-1):
            
            E = 100000
            for shift in xy_shifts:
                diff = image.getpixel((x + shift[0], y + shift[1]))
                diff = diff - image.getpixel((x, y))
                diff = diff * diff
                if diff < E:
                    E = diff
            if E > threshold:
                output_img[y,x] = (0,0,255)

    cv2.imshow('Detected Corners', output_img)
    cv2.waitKey(0)
