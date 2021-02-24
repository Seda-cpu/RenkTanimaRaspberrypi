import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) 

while(1):
    _, imageFrame = cap.read()
    hsv_frame = cv.cvtColor(imageFrame, cv.COLOR_BGR2HSV)
    
    low_red = np.array([161,155,84])
    high_red = np.array([179,255,255])
    red_mask = cv.inRange(hsv_frame, low_red, high_red)
    red= cv.bitwise_and(imageFrame,imageFrame, mask=red_mask) #görüntü üzerinde aritmetik işlemler 
    
        
    """
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv.inRange(hsv_frame, low_blue, high_blue)
    blue = cv.bitwise_and(frame, frame, mask=blue_mask)
    
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv.inRange(hsv_frame, low_green, high_green)
    green = cv.bitwise_and(frame, frame, mask=green_mask)
    
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv.inRange(hsv_frame, low, high)
    result = cv.bitwise_and(frame, frame, mask=mask)
    """
    kernal = np.ones((5, 5), "uint8")
    
    red_mask = cv.dilate(red_mask, kernal) 
    res_red = cv.bitwise_and(imageFrame, imageFrame,  mask = red_mask)
    
    contours, hierarchy = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours): 
        area = cv.contourArea(contour) 
        if(area > 300): 
            x, y, w, h = cv.boundingRect(contour) 
            imageFrame = cv.rectangle(imageFrame, (x, y),  (x + w, y + h),  (0, 0, 255), 2) 
              
            cv.putText(imageFrame, "Kirmizi", (x, y), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))
            
            
            
    
    cv.imshow('frame',imageFrame)
    cv.imshow('kirmizi',red)
    cv.imshow('mask',red_mask)
    #cv.imshow('blue',blue)
    #cv.imshow('green',green)
    #cv.imshow('result',result)
    k=cv.waitKey(5) & 0xFF
    if k == 27:
        cap.release() 
        cv.destroyAllWindows()
        break
cv.destroyAllWindows()
