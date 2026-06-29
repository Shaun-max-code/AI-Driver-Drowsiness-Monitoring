import cv2

from src.camera import Camera
from src.face_mesh import FaceLandmarker
from src.constants import LEFT_EYE, RIGHT_EYE
from src.detectors.eye_detector import EyeDetector
from src.detectors.blink_detector import BlinkDetector


def main():

    camera = Camera()
    face_mesh = FaceLandmarker()

    eye_detector = EyeDetector()
    blink_detector = BlinkDetector()

    while True:

        frame = camera.read()

        if frame is None:
            break

        result = face_mesh.detect(frame)

        if result.multi_face_landmarks:

            h, w, _ = frame.shape

            for face in result.multi_face_landmarks:

                # Get eye landmarks
                left_eye = eye_detector.get_eye_points(
                    face,
                    LEFT_EYE,
                    w,
                    h,
                )

                right_eye = eye_detector.get_eye_points(
                    face,
                    RIGHT_EYE,
                    w,
                    h,
                )

                # Calculate EAR
                left_ear = blink_detector.calculate_ear(left_eye)
                right_ear = blink_detector.calculate_ear(right_eye)

                ear = (left_ear + right_ear) / 2

                # Update blink detector
                blink_detector.update(ear)

                blink_count = blink_detector.get_count()

                # Draw left eye landmarks
                for point in left_eye:

                    x, y = point.astype(int)

                    cv2.circle(
                        frame,
                        (x, y),
                        3,
                        (0, 255, 0),
                        -1,
                    )

                # Draw right eye landmarks
                for point in right_eye:

                    x, y = point.astype(int)

                    cv2.circle(
                        frame,
                        (x, y),
                        3,
                        (0, 255, 0),
                        -1,
                    )

                # Display EAR
                cv2.putText(
                    frame,
                    f"EAR: {ear:.2f}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2,
                )

                # Display Blink Count
                cv2.putText(
                    frame,
                    f"Blinks: {blink_count}",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2,
                )

        cv2.imshow("AI Driver Monitoring", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == 27:  # ESC
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()