import cv2 
vidL = cv2.VideoCapture(2) 
vidR = cv2.VideoCapture(4)
i = 0
p = 0
while(True): 
    ret, frameL = vidL.read() 
    ret, frameR = vidR.read() 
    cv2.imshow('frameR', frameR)
    cv2.imshow('frameL', frameL)
    if i == 100:
        print("writing")
        cv2.imwrite("/home/guru/stereo_vision/calib_images/left/left_"+str(p)+".jpg", frameL)
        cv2.imwrite("/home/guru/stereo_vision/calib_images/right/right_"+str(p)+".jpg", frameR)
        p+=1
        i = 0
    i+=1
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

vidL.release()
vidR.release() 
cv2.destroyAllWindows() 
