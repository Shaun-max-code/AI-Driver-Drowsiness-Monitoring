import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

print(frame[240, 320])

cap.release()