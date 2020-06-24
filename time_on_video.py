import cv2
from datetime import datetime as dt


cap = cv2.VideoCapture(0)

cap.set(3,1280)
cap.set(4,720)
print(dt.now())

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"WID: {cap.get(3)}, HIG: {cap.get(4)}"
        frame = cv2.putText(frame, str(dt.now()), (10,50),font,1,(0,255,0),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
