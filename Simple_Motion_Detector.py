from imutils.video import VideoStream
import imutils
import argparse
import cv2
import numpy as np
import time
import datetime
from live_cam import live


ap = argparse.ArgumentParser()
ap.add_argument("-v","--video",help="Path to video")
ap.add_argument("-a","--area",type = int,default = 500, help="min area")

args = vars(ap.parse_args())

print(args)

if args.get("video",None) is None:
    vs = VideoStream(src=0).start()
    # vs = live()
    time.sleep(2.0)
else:
    vs = cv2.VideoCapture(args["video"])

firstFrame = None

fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    # frame = live()
    frame = vs.read()

    frame = frame if args.get("video",None) is None else frame[1]
    text = "Unoccupied"

    if frame is None:
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    if firstFrame is None:
        firstFrame = gray
        continue

    # frameDelta = cv2.absdiff(firstFrame,gray)
    frameDelta = fgbg.apply(gray)
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # print(len(cnts))
    n=0
    for c in cnts:

        if cv2.contourArea(c) < args["area"]:
            continue
        n+=1
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y) ,(x+w,y+h), (0,255,0), 2)
        text = "Occupied"

    cv2.putText(frame, f"Room Status:{text}",(10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
    cv2.putText(frame,f"Total Objects : {n} "+ datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    cv2.imshow("Security Feed", frame)
    cv2.imshow("Thresh",thresh)
    cv2.imshow("Frame Delta",frameDelta)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

vs.stop() if args.get("video", None) is None else vs.release()
cv2.destroyAllWindows()
