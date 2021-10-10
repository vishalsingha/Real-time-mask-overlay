# import library
import cv2
import numpy as np
import face_recognition
import matplotlib.pyplot as plt

# load overlay image
img_overlay_orig = cv2.imread("mask.png", cv2.IMREAD_UNCHANGED)

# initialize camara
cam = cv2.VideoCapture(0)
while 1:
    _, img = cam.read()
    if(_):
        img_overlay = img_overlay_orig.copy()
        # locate face
        face_loc = face_recognition.face_locations(img, model="cnn")
        if (len(face_loc)!=0):
            for face in face_loc:
                r = ((face[1]-face[3])*0.65)/img_overlay.shape[0]
                # resize overlay to required size
                img_overlay = cv2.resize(img_overlay, (0, 0), None, r, r)
                x, y = img_overlay.shape[0], img_overlay.shape[1]
                d_p = int((y-(face[1]-face[3]))/2)
                #  region of image for pasting overlay
                roi_img = img[(int((face[0]+face[2])/2)-x+4):int((face[0]+face[2])/2+4), (face[3]-d_p+3):(face[3]-d_p)+y+3, :]
                for i in range(x):
                    for j in range(y):
                        if(img_overlay[i, j, 3]>0):
                            roi_img[i, j, :] = img_overlay[i, j, 0:3]
        cv2.imshow('img',img)
    if cv2.waitKey(30) & 0xff == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
