import cv2
import time

from src.camera import Camera
from src.face_landmarker import FaceLandmarker


def main():

    camera = Camera()
    landmarker = FaceLandmarker()

    while True:

        frame = camera.read()

        if frame is None:
            break

        timestamp = int(time.time() * 1000)

        result = landmarker.detect(frame, timestamp)

        cv2.putText(
            frame,
            f"Faces: {len(result.face_landmarks)}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("AI Driver Monitoring", frame)

        if cv2.waitKey(1) == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()