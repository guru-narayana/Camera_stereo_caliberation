import cv2
import numpy as np
import glob
dirpath = "/home/guru/stereo_vision/calib_images/left"
prefix = "left_"
image_format = "jpg"
square_size = 2.1
width = 9
height = 7

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((height*width, 3), np.float32)
objp[:, :2] = np.mgrid[0:width, 0:height].T.reshape(-1, 2)
objp = objp * square_size
objpoints = []
imgpoints = []
images = glob.glob(dirpath+'/' + prefix + '*.' + image_format)

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, (width, height), None)
    if ret:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)
        img = cv2.drawChessboardCorners(img, (width, height), corners2, ret)

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

if ret:
    print(mtx)
    print(dist)

np.savetxt('left_dist.csv', dist, delimiter=',')
np.savetxt('left_mtx.csv', mtx, delimiter=',')