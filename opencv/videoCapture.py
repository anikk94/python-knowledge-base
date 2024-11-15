# basic example of capturing image frames from a video source using openCV
import cv2

webcam = 0
realsensecam = 1

cap = cv2.VideoCapture(realsensecam)

if not cap.isOpened():
    print("problem opening camera")
    exit()

while True:
    returnValue, frame = cap.read()

    if not returnValue:
        print("Failed to read image")
        break

    cv2.imshow("camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
