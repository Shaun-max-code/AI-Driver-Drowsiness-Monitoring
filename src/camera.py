import cv2

class Camera:

    def __init__(self, index=0):
        self.cap = cv2.VideoCapture(index)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        if not self.cap.isOpened():
            raise RuntimeError("Could not open camera.")

    def read(self):
        ret, frame = self.cap.read()

        if not ret:
            return None

        return cv2.flip(frame, 1)

    def release(self):
        self.cap.release()