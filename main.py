import cv2
from src.camera import Camera
from src.face_detection import FaceDetector


def main():
    camera = Camera()
    detector = FaceDetector()   # <-- Create the detector

    while True:
        frame = camera.read()

        if frame is None:
            break

        # Detect faces
        frame = detector.detect(frame)

        cv2.putText(
            frame,
            "AI Driver Drowsiness Monitoring",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("AI Driver Monitoring", frame)

        key = cv2.waitKey(1)

        if key == 27:  # ESC
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()