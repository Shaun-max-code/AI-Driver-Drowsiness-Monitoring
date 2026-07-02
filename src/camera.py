import cv2

class Camera:

    def __init__(self, index=1):
        self.cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        if not self.cap.isOpened():
            raise RuntimeError(f"Could not open camera {index}.")

    def read(self):
        ret, frame = self.cap.read()

        if not ret:
            return None

        return cv2.flip(frame, 1)

    def release(self):
        self.cap.release()